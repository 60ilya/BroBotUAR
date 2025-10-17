import sqlite3
import logging
import json
from pathlib import Path
from config import Config

class Database:
    def __init__(self, db_path: str = Config.DATABASE_URL):
        self.db_path = db_path
        Path("data").mkdir(exist_ok=True)
        self.init_database()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_database(self):
        """Инициализация базы данных и создание таблиц"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Таблица users
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tg_id INTEGER UNIQUE NOT NULL,
                        username TEXT,
                        full_name TEXT,
                        is_admin BOOLEAN DEFAULT FALSE,
                        notifications BOOLEAN DEFAULT TRUE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Таблица requests
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS requests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        type TEXT NOT NULL,
                        text TEXT,
                        duration_days INTEGER DEFAULT 14,
                        media_paths TEXT,
                        status TEXT DEFAULT 'pending',
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                    )
                ''')
                
                conn.commit()
                logging.info("Database tables created successfully")
                
        except Exception as e:
            logging.error(f"Error creating database tables: {e}")

    # ===== USER FUNCTIONS =====

    def add_user(self, tg_id: int, username: str = None, full_name: str = None, is_admin: bool = False) -> bool:
        """Добавление нового пользователя"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR IGNORE INTO users (tg_id, username, full_name, is_admin)
                    VALUES (?, ?, ?, ?)
                ''', (tg_id, username, full_name, is_admin))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logging.error(f"Error adding user: {e}")
            return False

    def get_user(self, tg_id: int):
        """Получение пользователя по tg_id"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM users WHERE tg_id = ?
                ''', (tg_id,))
                row = cursor.fetchone()
                if row:
                    return {
                        'id': row[0],
                        'tg_id': row[1],
                        'username': row[2],
                        'full_name': row[3],
                        'is_admin': bool(row[4]),
                        'notifications': bool(row[5]),
                        'created_at': row[6],
                        'updated_at': row[7]
                    }
                return None
        except Exception as e:
            logging.error(f"Error getting user: {e}")
            return None

    def get_user_by_id(self, user_id: int):
        """Получение пользователя по id"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
                row = cursor.fetchone()
                if row:
                    return {
                        'id': row[0],
                        'tg_id': row[1],
                        'username': row[2],
                        'full_name': row[3],
                        'is_admin': bool(row[4]),
                        'notifications': bool(row[5]),
                        'created_at': row[6],
                        'updated_at': row[7]
                    }
                return None
        except Exception as e:
            logging.error(f"Error getting user by id: {e}")
            return None

    def update_user(self, tg_id: int, username: str = None, full_name: str = None, 
                   notifications: bool = None) -> bool:
        """Обновление данных пользователя"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Собираем поля для обновления
                update_fields = []
                params = []
                
                if username is not None:
                    update_fields.append("username = ?")
                    params.append(username)
                if full_name is not None:
                    update_fields.append("full_name = ?")
                    params.append(full_name)
                if notifications is not None:
                    update_fields.append("notifications = ?")
                    params.append(notifications)
                
                update_fields.append("updated_at = CURRENT_TIMESTAMP")
                params.append(tg_id)
                
                query = f"UPDATE users SET {', '.join(update_fields)} WHERE tg_id = ?"
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logging.error(f"Error updating user: {e}")
            return False

    def set_user_admin(self, tg_id: int, is_admin: bool = True) -> bool:
        """Назначение/снятие прав администратора"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE users SET is_admin = ?, updated_at = CURRENT_TIMESTAMP 
                    WHERE tg_id = ?
                ''', (is_admin, tg_id))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logging.error(f"Error setting user admin: {e}")
            return False
        
    def set_user_notification(self, tg_id: int, notification: bool = True) -> bool:
        """Получение уведомлений"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE users SET notifications = ?, updated_at = CURRENT_TIMESTAMP 
                    WHERE tg_id = ?
                ''', (notification, tg_id))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logging.error(f"Error setting user notification: {e}")
            return False

    def get_all_admins(self):
        """Получение всех администраторов"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE is_admin = TRUE')
                return [
                    {
                        'id': row[0],
                        'tg_id': row[1],
                        'username': row[2],
                        'full_name': row[3],
                        'is_admin': bool(row[4]),
                        'notifications': bool(row[5]),
                        'created_at': row[6],
                        'updated_at': row[7]
                    }
                    for row in cursor.fetchall()
                ]
        except Exception as e:
            logging.error(f"Error getting admins: {e}")
            return []

    def get_all_users(self):
        """Получение всех пользователей"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users ORDER BY created_at DESC')
                return [
                    {
                        'id': row[0],
                        'tg_id': row[1],
                        'username': row[2],
                        'full_name': row[3],
                        'is_admin': bool(row[4]),
                        'notifications': bool(row[5]),
                        'created_at': row[6],
                        'updated_at': row[7]
                    }
                    for row in cursor.fetchall()
                ]
        except Exception as e:
            logging.error(f"Error getting all users: {e}")
            return []

    def user_exists(self, tg_id: int) -> bool:
        """Проверка существования пользователя"""
        return self.get_user(tg_id) is not None

    # ===== REQUEST FUNCTIONS =====

    def add_request(self, user_id: int, request_type: str, duration_days: int, text: str = None,
                   media_paths = None, status: str = 'pending'):
        """Добавление новой заявки"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Преобразуем список путей в JSON строку
                media_json = json.dumps(media_paths) if media_paths else None
                
                cursor.execute('''
                    INSERT INTO requests (user_id, type, text, duration_days, media_paths, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (user_id, request_type, duration_days, text, media_json, status))
                
                conn.commit()
                return cursor.lastrowid
        except Exception as e:
            logging.error(f"Error adding request: {e}")
            return None

    def get_request(self, request_id: int):
        """Получение заявки по ID"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT r.*, u.tg_id, u.username, u.full_name 
                    FROM requests r 
                    JOIN users u ON r.user_id = u.id 
                    WHERE r.id = ?
                ''', (request_id,))
                row = cursor.fetchone()
                if row:
                    return {
                        'id': row[0],
                        'user_id': row[1],
                        'type': row[2],
                        'text': row[3],
                        'media_paths': json.loads(row[4]) if row[4] else [],
                        'status': row[5],
                        'created_at': row[6],
                        'updated_at': row[7],
                        'user_tg_id': row[8],
                        'user_username': row[9],
                        'user_full_name': row[10]
                    }
                return None
        except Exception as e:
            logging.error(f"Error getting request: {e}")
            return None

    def get_user_requests(self, user_id: int, limit: int = None):
        """Получение заявок пользователя"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                query = '''
                    SELECT * FROM requests 
                    WHERE user_id = ? 
                    ORDER BY created_at DESC
                '''
                params = [user_id]
                
                if limit:
                    query += ' LIMIT ?'
                    params.append(limit)
                
                cursor.execute(query, params)
                return [
                    {
                        'id': row[0],
                        'user_id': row[1],
                        'type': row[2],
                        'text': row[3],
                        'media_paths': json.loads(row[4]) if row[4] else [],
                        'status': row[5],
                        'created_at': row[6],
                        'updated_at': row[7]
                    }
                    for row in cursor.fetchall()
                ]
        except Exception as e:
            logging.error(f"Error getting user requests: {e}")
            return []

    def get_requests_by_type(self, request_type: str, status: str = None, 
                           limit: int = None):
        """Получение заявок по типу"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                query = '''
                    SELECT r.*, u.tg_id, u.username, u.full_name 
                    FROM requests r 
                    JOIN users u ON r.user_id = u.id 
                    WHERE r.type = ?
                '''
                params = [request_type]
                
                if status:
                    query += ' AND r.status = ?'
                    params.append(status)
                
                query += ' ORDER BY r.created_at DESC'
                
                if limit:
                    query += ' LIMIT ?'
                    params.append(limit)
                
                cursor.execute(query, params)
                return [
                    {
                        'id': row[0],
                        'user_id': row[1],
                        'type': row[2],
                        'text': row[3],
                        'duration_days': row[4],
                        'media_paths': json.loads(row[5]) if row[5] else [],
                        'status': row[6],
                        'created_at': row[7],
                        'updated_at': row[8],
                        'user_tg_id': row[9],
                        'user_username': row[10],
                        'user_full_name': row[11]
                    }
                    for row in cursor.fetchall()
                ]
        except Exception as e:
            logging.error(f"Error getting requests by type: {e}")
            return []

    def get_pending_requests(self, limit: int = None):
        """Получение ожидающих заявок"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                query = '''
                    SELECT r.*, u.tg_id, u.username, u.full_name 
                    FROM requests r 
                    JOIN users u ON r.user_id = u.id 
                    WHERE r.status = 'pending'
                    ORDER BY r.created_at DESC
                '''
                params = []
                if limit:
                    query += ' LIMIT ?'
                    params.append(limit)
                
                cursor.execute(query, params)
                return [
                    {
                        'id': row[0],
                        'user_id': row[1],
                        'type': row[2],
                        'text': row[3],
                        'duration_days': row[4],
                        'media_paths': json.loads(row[5]) if row[5] else [],
                        'status': row[6],
                        'created_at': row[7],
                        'updated_at': row[8],
                        'user_tg_id': row[9],
                        'user_username': row[10],
                        'user_full_name': row[11]
                    }
                    for row in cursor.fetchall()
                ]
        except Exception as e:
            logging.error(f"Error getting pending requests: {e}")
            return []

    def update_request_status(self, request_id: int, status: str) -> bool:
        """Обновление статуса заявки"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE requests 
                    SET status = ?, updated_at = CURRENT_TIMESTAMP 
                    WHERE id = ?
                ''', (status, request_id))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logging.error(f"Error updating request status: {e}")
            return False

    def delete_request(self, request_id: int) -> bool:
        """Удаление заявки"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM requests WHERE id = ?', (request_id,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logging.error(f"Error deleting request: {e}")
            return False

    def get_requests_count(self, status: str = None) -> int:
        """Получение количества заявок"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if status:
                    cursor.execute('SELECT COUNT(*) FROM requests WHERE status = ?', (status,))
                else:
                    cursor.execute('SELECT COUNT(*) FROM requests')
                return cursor.fetchone()[0]
        except Exception as e:
            logging.error(f"Error getting requests count: {e}")
            return 0

    # ===== STATISTICS FUNCTIONS =====

    def get_user_count(self) -> int:
        """Получение общего количества пользователей"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT COUNT(*) FROM users')
                return cursor.fetchone()[0]
        except Exception as e:
            logging.error(f"Error getting user count: {e}")
            return 0

    def get_requests_statistics(self):
        """Получение статистики по заявкам"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Общее количество заявок
                cursor.execute('SELECT COUNT(*) FROM requests')
                total = cursor.fetchone()[0]
                
                # Количество по статусам
                cursor.execute('''
                    SELECT status, COUNT(*) 
                    FROM requests 
                    GROUP BY status
                ''')
                status_stats = {row[0]: row[1] for row in cursor.fetchall()}
                
                # Количество по типам
                cursor.execute('''
                    SELECT type, COUNT(*) 
                    FROM requests 
                    GROUP BY type
                ''')
                type_stats = {row[0]: row[1] for row in cursor.fetchall()}
                
                return {
                    'total_requests': total,
                    'by_status': status_stats,
                    'by_type': type_stats
                }
        except Exception as e:
            logging.error(f"Error getting requests statistics: {e}")
            return {'total_requests': 0, 'by_status': {}, 'by_type': {}}