from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CopyTextButton

def back_start_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
         [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
       
    
def start_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Афиша событий', callback_data='events'),
         InlineKeyboardButton(text='Конструктор маршрута', callback_data='routes')],
        [InlineKeyboardButton(text='Жилье и недвижимость', callback_data='housing'),
         InlineKeyboardButton(text='Транспорт и аренда', callback_data='transport')],
        [InlineKeyboardButton(text='Объявления и услуги', callback_data='adverts'),
         InlineKeyboardButton(text='Контакты и поддержка', callback_data='contacts')]
    ])
    
def events_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Афиша месяца', callback_data='events_month'),
         InlineKeyboardButton(text='🎤 Добавить свое мероприятие', callback_data='events_request')],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def events_month_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📅 События недели', url='https://t.me/capetown_uar/999'),
         InlineKeyboardButton(text='🗓 События месяца', url='https://t.me/capetown_uar/978')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='events'),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def events_month_request():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Хочу в афишу на месяц', callback_data='events_month_request_chat')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='events'),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def events_month_request(is_monthly: bool = False):
    """Клавиатура с toggle кнопкой для выбора длительности"""
    toggle_text = "✅ Афиша месяца (30 дней)" if is_monthly else "✅ Афиша недели (14 дней)"
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=toggle_text, callback_data="events_duration")],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='events'),
            InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')
        ]
    ])
    
def events_request_ikb():

    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='events'),
            InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')
        ]
    ])
    
    
def routes_menu(notification: bool = False):
    if notification:
        notification_text = "✅ Ждем уведомления"
    else:
        notification_text = "🔔 Хочу уведомление о запуске"
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=notification_text, callback_data="routes_notification")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])


def housing_menu_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🏡 Посмотреть объявления', url='https://t.me/+DNgqJjmx55A1YjYy')],
        [InlineKeyboardButton(text='➕ Подать объявление', callback_data='housing_request'),
         InlineKeyboardButton(text='💰 Продажа/покупка', callback_data='housing_rent')],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def housing_rent_ikb(text_template):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Копировать шаблон', copy_text=CopyTextButton(text=text_template))],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='housing'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def housing_request_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🔙 Назад', callback_data='housing'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def transport_menu_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🚘 Смотреть каталог', callback_data='transport_catalog')],
        [InlineKeyboardButton(text='Купить автомобиль', url='https://t.me/adelsuprun'),
         InlineKeyboardButton(text='Оставить отзыв', url='https://t.me/adelsuprun')],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def transport_catalog_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сайт-агрегатор', callback_data='transport_agregator'),
         InlineKeyboardButton(text='Местные партнеры', callback_data='transport_partners')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='transport'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def transport_partners_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Партнер 1', callback_data='transport_partner_1'),
         InlineKeyboardButton(text='Партнер 2', callback_data='transport_partner_2')],
        [InlineKeyboardButton(text='Партнер 3', callback_data='transport_partner_3')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='transport'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def transport_agregator_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='TRIP.COM - транспорт', url='https://www.trip.com/t/AHvHi7zZqR2')],
        [InlineKeyboardButton(text='TRIP.COM - главная', url='https://www.trip.com/t/FVnSCs0aqR2')],
        [InlineKeyboardButton(text='TRIP.COM - трансфер', url='https://www.trip.com/t/AZXPqE3aqR2')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='transport'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def transport_request_ikb(url):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Забронировать', url=url)],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='transport_partners'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def adverts_menu_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🏡 Посмотреть объявления', url='https://t.me/capetownads')],
        [InlineKeyboardButton(text='➕ Подать объявление', callback_data='adverts_request')]
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def adverts_request_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🔙 Назад', callback_data='adverts'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def contacts_menu_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Визы и юр. услуги', callback_data='contacts_visa'),
         InlineKeyboardButton(text='💰 Обмен', callback_data='contacts_exchange')],
        [InlineKeyboardButton(text='Обманули? (раздел помощи)', callback_data='contacts_lie'),
        InlineKeyboardButton(text='🧑‍💻 Разработка ботов и др.', url='t.me/pybuuuk')],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def contacts_exchange_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🔙 Назад', callback_data='contacts'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def contacts_card_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Заказать карту', url='t.me/oplatagurucardsbot')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='contacts'),
        InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def admin_menu_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Заявки', callback_data='admin_requests')],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def request_action_ikb(request_id: int, current_index: int, total_requests: int):
    """Клавиатура действий для заявки с пагинацией"""
    keyboard = []
    
    # Кнопки действий
    keyboard.append([
        InlineKeyboardButton(text="✔️ Принять", callback_data=f"admin_accept_{request_id}"),
        InlineKeyboardButton(text="✖️ Отклонить", callback_data=f"admin_decline_{request_id}")
    ])

    # Кнопки пагинации
    nav_buttons = []
    if current_index > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️ Предыдущая", callback_data=f"admin_prev_{current_index}"))
    
    nav_buttons.append(InlineKeyboardButton(text=f"{current_index + 1}/{total_requests}", callback_data="admin_current_page"))
    
    if current_index < total_requests - 1:
        nav_buttons.append(InlineKeyboardButton(text="Следующая ➡️", callback_data=f"admin_next_{current_index}"))
    
    if nav_buttons:
        keyboard.append(nav_buttons)
    
    keyboard.append([InlineKeyboardButton(text="🔙 Назад", callback_data="admin")])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def admin_request_confirm_ikb(request_id: int):
    """Клавиатура для подтверждения принятия"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✔️ Да, принять заявку", callback_data=f"admin_confirm_accept_{request_id}")],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data=f"admin_cancel_accept_{request_id}")]
        ]
    )
