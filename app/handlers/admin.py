import logging
from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from config import Config
from db import Database
from keyboards.inline import admin_menu_ikb, back_start_menu, request_action_ikb, admin_request_confirm_ikb

router = Router()
db = Database()

# Состояния для FSM
class AdminRequestStates(StatesGroup):
    waiting_decline_reason = State()
    waiting_accept_confirmation = State()


@router.callback_query(F.data == 'admin')
async def adverts_menu(callback: types.CallbackQuery):
    text = """Меню администратора"""
    
    if callback.from_user.id not in Config.ADMIN_IDS:
        return False
    
    try:
        await callback.message.edit_text(
            text,
            reply_markup=admin_menu_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.delete()
        await callback.message.answer(
            text,
            reply_markup=admin_menu_ikb(),
            parse_mode="HTML")
  
@router.message(Command('admin'))
async def adverts_menu(message: types.Message):
    text = """Меню администратора"""
    
    if message.from_user.id not in Config.ADMIN_IDS:
        return False
    
    await message.answer(
        text,
        reply_markup=admin_menu_ikb(),
        parse_mode="HTML")


@router.callback_query(F.data == 'admin_requests')
async def admin_requests(callback: types.CallbackQuery):
    """Просмотр первой заявки"""
    requests = db.get_pending_requests()
    
    if not requests:
        await callback.message.edit_text(
            "Нет ожидающих заявок",
            reply_markup=back_start_menu()
        )
        return
    
    # Показываем первую заявку
    await show_request(callback, requests, 0)

async def show_request(callback: types.CallbackQuery, requests: list, index: int):
    """Показать заявку по индексу"""
    request = requests[index]
    
    # Формируем текст заявки
    text = f"""
📋 <b>Заявка #{request['id']}</b>

👤 <b>Пользователь:</b>
├ ID: {request['user_tg_id']}
├ Username: @{request['user_username'] or 'не указан'}
└ Имя: {request['user_full_name'] or 'не указано'}

⏱ <b>Длительность:</b> {request['duration_days']} дней
📅 <b>Дата подачи:</b> {request['created_at']}

<b>Текст заявки:</b>
{request['text']}
"""
    
    # Если есть медиафайлы
    if request['media_paths']:
        text += f"\n📎 <b>Медиафайлы:</b> {len(request['media_paths'])} шт."
        
        # Отправляем первое фото по file_id
        try:
            first_file_id = request['media_paths'][0]
            
            await callback.message.answer_photo(
                photo=first_file_id,
                caption=text,
                reply_markup=request_action_ikb(request['id'], index, len(requests)),
                parse_mode="HTML"
            )
            return
            
        except Exception as e:
            logging.error(f"Error sending photo: {e}")
            # Если не удалось отправить фото, отправляем текстовое сообщение
            text += f"\n\n❌ <i>Не удалось загрузить фото</i>"
    
    try:
        # Если нет фото или произошла ошибка, отправляем текстовое сообщение
        await callback.message.edit_text(
            text=text,
            reply_markup=request_action_ikb(request['id'], index, len(requests)),
            parse_mode="HTML"
        )
    except:
        await callback.message.delete()
        await callback.message.answer(
            text=text,
            reply_markup=request_action_ikb(request['id'], index, len(requests)),
            parse_mode="HTML"
        )

@router.callback_query(F.data.startswith('admin_prev_'))
async def show_previous_request(callback: types.CallbackQuery):
    """Показать предыдущую заявку"""
    index = int(callback.data.split('_')[2])
    requests = db.get_pending_requests()
    
    if index > 0:
        await show_request(callback, requests, index - 1)
    else:
        await callback.answer("Это первая заявка")

@router.callback_query(F.data.startswith('admin_next_'))
async def show_next_request(callback: types.CallbackQuery):
    """Показать следующую заявку"""
    index = int(callback.data.split('_')[2])
    requests = db.get_pending_requests()
    
    if index < len(requests) - 1:
        await show_request(callback, requests, index + 1)
    else:
        await callback.answer("Это последняя заявка")

@router.callback_query(F.data.startswith('admin_accept_'))
async def accept_request(callback: types.CallbackQuery, state: FSMContext):
    """Начало процесса принятия заявки"""
    request_id = int(callback.data.split('_')[2])
    
    # Получаем текущий индекс и данные заявки
    requests = db.get_pending_requests()
    current_index = 0
    request_data = None
    for i, req in enumerate(requests):
        if req['id'] == request_id:
            current_index = i
            request_data = req
            break
    
    if not request_data:
        await callback.answer("Заявка не найдена", show_alert=True)
        return
    
    # Сохраняем данные в состоянии
    await state.update_data(
        request_id=request_id,
        current_index=current_index,
        total_requests=len(requests)
    )
    await state.set_state(AdminRequestStates.waiting_accept_confirmation)
    
    # Показываем подтверждение
    text = f"""
⚠️ <b>Подтверждение принятия</b>

Вы уверены, что хотите принять эту заявку?

📋 <b>Заявка #{request_id}</b>
👤 <b>Пользователь:</b> {request_data['user_full_name'] or request_data['user_username'] or f"ID: {request_data['user_tg_id']}"}
⏱ <b>Длительность:</b> {request_data['duration_days']} дней

<b>Текст заявки:</b>

{request_data['text']}
"""
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=admin_request_confirm_ikb(request_id),
            parse_mode="HTML"
        )
    except:
        await callback.message.delete()
        await callback.message.answer(
            text=text,
            reply_markup=admin_request_confirm_ikb(request_id),
            parse_mode="HTML"
        )

@router.callback_query(F.data.startswith('admin_confirm_accept_'))
async def confirm_accept_request(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    """Подтверждение принятия заявки"""
    request_id = int(callback.data.split('_')[3])
    
    # Получаем данные из состояния
    user_data = await state.get_data()
    current_index = user_data.get('current_index', 0)
    total_requests = user_data.get('total_requests', 0)
    
    # Обновляем статус заявки
    if db.update_request_status(request_id, 'approved'):
        # Получаем данные заявки для отправки в канал
        request = db.get_request_by_id(request_id)
        
        if request:
            # Формируем сообщение для канала
            channel_text = request['text']
            
            # Отправляем в канал и получаем сообщение
            try:
                message_in_channel = None
                # Если есть медиафайлы, отправляем с первым медиа
                if request['media_paths']:
                    first_file_id = request['media_paths'][0]
                    message_in_channel = await bot.send_photo(
                        chat_id=Config.CHANNEL_ID,
                        photo=first_file_id,
                        caption=channel_text,
                        parse_mode="HTML"
                    )
                else:
                    # Если нет медиа, отправляем просто текст
                    message_in_channel = await bot.send_message(
                        chat_id=Config.CHANNEL_ID,
                        text=channel_text,
                        parse_mode="HTML"
                    )
                
                # Формируем ссылку на пост в канале
                if message_in_channel:
                    # Для публичного канала
                    if hasattr(Config, 'CHANNEL_USERNAME') and Config.CHANNEL_USERNAME:
                        channel_username = Config.CHANNEL_USERNAME.lstrip('@')
                        post_url = f"https://t.me/{channel_username}/{message_in_channel.message_id}"
                    else:
                        # Для приватного канала (если бот админ)
                        post_url = f"https://t.me/c/{str(Config.CHANNEL_ID).replace('-100', '')}/{message_in_channel.message_id}"
                    
                    # Уведомляем пользователя с ссылкой на пост
                    user_notification = f"""
✅ Ваша заявка была принята!

📢 Опубликовано в канале: {post_url}

Спасибо, что выбрали нас! 🚗
"""
                else:
                    user_notification = "✅ Ваша заявка была принята!"
                
            except Exception as e:
                logging.error(f"Error sending to channel: {e}")
                user_notification = "✅ Ваша заявка была принята!"
            
            # Уведомляем пользователя
            try:
                await bot.send_message(
                    chat_id=request['user_tg_id'],
                    text=user_notification,
                    disable_web_page_preview=True
                )
            except Exception as e:
                logging.error(f"Error notifying user: {e}")
        
        # Очищаем состояние
        await state.clear()
        
        # Показываем следующую заявку или возвращаем в меню
        remaining_requests = db.get_pending_requests()
        
        if remaining_requests:
            new_index = min(current_index, len(remaining_requests) - 1)
            await show_request(callback, remaining_requests, new_index)
            await callback.answer("✅ Заявка принята", show_alert=True)
        else:
            await callback.message.edit_text(
                "✅ Заявка принята и отправлена в канал\n\n",
                reply_markup=back_start_menu()
            )
    else:
        await callback.answer("Ошибка при принятии заявки", show_alert=True)

@router.callback_query(F.data.startswith('admin_cancel_accept_'))
async def cancel_accept_request(callback: types.CallbackQuery, state: FSMContext):
    """Отмена принятия заявки"""
    request_id = int(callback.data.split('_')[3])
    
    # Очищаем состояние
    await state.clear()
    
    # Возвращаемся к просмотру заявки
    requests = db.get_pending_requests()
    current_index = 0
    for i, req in enumerate(requests):
        if req['id'] == request_id:
            current_index = i
            break
    
    await show_request(callback, requests, current_index)

@router.callback_query(F.data.startswith('admin_decline_'))
async def decline_request(callback: types.CallbackQuery, state: FSMContext):
    """Начало процесса отклонения заявки"""
    request_id = int(callback.data.split('_')[2])
    
    # Получаем текущий индекс для восстановления после отклонения
    requests = db.get_pending_requests()
    current_index = 0
    for i, req in enumerate(requests):
        if req['id'] == request_id:
            current_index = i
            break
    
    # Сохраняем ID заявки и индекс в состоянии
    await state.update_data(request_id=request_id, current_index=current_index)
    await state.set_state(AdminRequestStates.waiting_decline_reason)
    
    await callback.message.edit_text(
        f"📝 <b>Отклонение заявки #{request_id}</b>\n\nВведите причину отклонения:",
        parse_mode="HTML",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[[
                types.InlineKeyboardButton(text="К заявкам", callback_data="admin_requests")
            ]]
        )
    )


@router.message(AdminRequestStates.waiting_decline_reason)
async def process_decline_reason(message: types.Message, state: FSMContext, bot: Bot):
    """Обработка причины отклонения"""
    decline_reason = message.text
    user_data = await state.get_data()
    request_id = user_data.get('request_id')
    current_index = user_data.get('current_index', 0)
    
    # Обновляем статус заявки
    if db.update_request_status(request_id, 'rejected'):
        # Получаем данные заявки для уведомления пользователя
        request = db.get_request_by_id(request_id)
        
        if request:
            # Уведомляем пользователя
            try:
                user_notification = f"""
❌ Ваша заявка была отклонена модератором. Вы можете подать новую заявку, учтите правки модератора 🧑‍💻

<b>Причина:</b>
{decline_reason}
"""
                await bot.send_message(
                    chat_id=request['user_tg_id'],
                    text=user_notification,
                    parse_mode="HTML"
                )
            except Exception as e:
                logging.error(f"Error notifying user: {e}")
        
        # Показываем следующую заявку или возвращаем в меню
        remaining_requests = db.get_pending_requests()
        
        if remaining_requests:
            new_index = min(current_index, len(remaining_requests) - 1)
            await message.answer(
                f"✅ Заявка #{request_id} отклонена",
                reply_markup=types.ReplyKeyboardRemove()
            )
            # Создаем новый callback для показа заявки
            callback = types.CallbackQuery(
                id="0",
                from_user=message.from_user,
                chat_instance="0",
                message=message,
                data=f"admin_requests"
            )
            await admin_requests(callback)
        else:
            await message.answer(
                "✅ Заявка отклонена, пользователь уведомлен",
                reply_markup=back_start_menu()
            )
    else:
        await message.answer(
            "❌ Ошибка при отклонении заявки",
            reply_markup=back_start_menu()
        )
    
    await state.clear()

# Отмена процесса отклонения
@router.callback_query(AdminRequestStates.waiting_decline_reason, F.data == "admin_requests")
async def cancel_decline(callback: types.CallbackQuery, state: FSMContext):
    """Отмена процесса отклонения заявки"""
    await state.clear()
    await admin_requests(callback)