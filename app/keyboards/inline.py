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
        [InlineKeyboardButton(text='➕ Подать объявление', callback_data='adverts_request')],
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

def routes_menu():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Задавай', callback_data="routes_start")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_start_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Нас двое', callback_data="routes_two"),
         InlineKeyboardButton(text='Самостоятельный трип', callback_data="routes_alone")],
        [InlineKeyboardButton(text='С семьей/с детьми', callback_data="routes_family"),
         InlineKeyboardButton(text='С друзьями', callback_data="routes_friends")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])


def routes_two_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Пешком + Такси + BUS', callback_data="routes_two_tran"),
         InlineKeyboardButton(text='Автомобиль / мотоцикл', callback_data="routes_two_him")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_int_ikb():
        return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Природа', callback_data="routes_two_nat"),
         InlineKeyboardButton(text='Еда и Напитки', callback_data="routes_two_food")],
        [InlineKeyboardButton(text='Животные', callback_data="routes_two_ani"),
         InlineKeyboardButton(text='Культурная программа', callback_data="routes_two_cult")],
        [InlineKeyboardButton(text='Экстрим', callback_data="routes_two_ext"),
         InlineKeyboardButton(text='Шопинг', callback_data="routes_two_shop")],
        [InlineKeyboardButton(text='Бары', callback_data="routes_two_bars"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_nat_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Парк', url="https://maps.app.goo.gl/icUHS8pKQXzeN9HF8"),
         InlineKeyboardButton(text='Водопад', url="https://maps.app.goo.gl/N6ujuLYG1BUPGofn6")],
        [InlineKeyboardButton(text='Локация из Pinterest', url="https://maps.app.goo.gl/MnznPUwgC1WXBAR5A"),
         InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_food_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Где позавтракать?', callback_data="routes_two_break"),
         InlineKeyboardButton(text='Где пообедать?', callback_data="routes_two_lun")],
        [InlineKeyboardButton(text='Где поужинать?', callback_data="routes_two_din"),
         InlineKeyboardButton(text='Кофейни', callback_data="routes_two_cof")],
        [InlineKeyboardButton(text='Матча', url="https://maps.app.goo.gl/RrfaL9A8K8XfevP2A?g_st=ipc"),
         InlineKeyboardButton(text='Другие напитки', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_two_break_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/YtjFVAvhP7F26CYN6"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/aRLYobWL6oVw8fKy5")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/66Vdw179gNjWaE1e7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/DAYpbSVYSLfhLNVx6")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/S41iJ7jToucgJy9m9")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/G2e415R866JJPiNeA")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_lun_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/KWCkZ1GSHyU2iApw7"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/AnNPag6tXSxT5ygL6")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/Eg3fB3gbnSGhfSJE7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/dT2w62n7xiRSJKZE8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/LvJTermoWYJRrbgA6")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/PixeH7D6Ds6Vkg26A")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_two_din_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/iiLUYdqktAzTvRs39"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/xxeJu2S5j8B2grRd8")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/UQDFUeU6xu8BBFzQ8"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/6scpUzcBJBKTkCGX7")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/y8eEY1nRyP9gXU3x7")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/Cv8XB3HtG89kuqwv9")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_cof_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/8LSUddTPq63YUxHN8"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/Kmmj2C9Eop46LSUWA")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/fodhkQhguoX8jiVA7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/Yhz1LX2jxhQiD3yf8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/M6jT9MZjMnu7SZM6A")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/o8mzJmTcqhxZWA228")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_ani_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Информация о путеводителе', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Винодельня с сафари', url="https://maps.app.goo.gl/4Ga7RW3ejPGLdcDr8?g_st=ipc")],
        [InlineKeyboardButton(text='Пингвины', url="https://maps.app.goo.gl/UEJxb4cBM7FQLNrL7?g_st=ipc"),
         InlineKeyboardButton(text='Птицы', url="https://maps.app.goo.gl/tzfTNASyxZyc3WBz8?g_st=ipc")],
        [InlineKeyboardButton(text='Морские котики', url="https://maps.app.goo.gl/5e7SS53VpDxL5iN68?g_st=ipc"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_cult_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Zeitz MOCAA', url="https://maps.app.goo.gl/3pqau2fVivFgTEUy6?g_st=ipc"),
         InlineKeyboardButton(text='Norval Foundation', url="https://maps.app.goo.gl/kgxewHb871qhJkfi7?g_st=ipc")],
        [InlineKeyboardButton(text='Музей шестого квартала', url="https://maps.app.goo.gl/TrnyhAEiCbzSFzaS7?g_st=ipc"),
         InlineKeyboardButton(text='Woodstock Exchange', url="https://maps.app.goo.gl/FhPsVXai8uc3JY2W6?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_ext_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_shop_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='AKJP STUDIO', url="https://maps.app.goo.gl/5hjyCXQrTKc8oBmM9"),
         InlineKeyboardButton(text='Century Blvd', url="https://maps.app.goo.gl/oXbZmN2xcQZpCqVb6")],
        [InlineKeyboardButton(text='The Old Biscuit Mill Market', url="https://maps.app.goo.gl/XECH1tm2ty7z5tv58"),
         InlineKeyboardButton(text='Vorster & Braye Ceramic Design', url="https://maps.app.goo.gl/KK632VZ4dwaRpf3G7")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ]) 

def routes_two_bars_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])


def routes_two_him_int_ikb():
        return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Природа', callback_data="routes_two_him_nat"),
         InlineKeyboardButton(text='Еда и Напитки', callback_data="routes_two_him_food")],
        [InlineKeyboardButton(text='Животные', callback_data="routes_two_him_ani"),
         InlineKeyboardButton(text='Культурная программа', callback_data="routes_two_him_cult")],
        [InlineKeyboardButton(text='Экстрим', callback_data="routes_two_him_ext"),
         InlineKeyboardButton(text='Шопинг', callback_data="routes_two_him_shop")],
        [InlineKeyboardButton(text='Бары', callback_data="routes_two_him_bars"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_him_nat_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Cape Point Vineyards Estate', url="https://maps.app.goo.gl/icUHS8pKQXzeN9HF8"),
         InlineKeyboardButton(text='Водопад', url="https://maps.app.goo.gl/N6ujuLYG1BUPGofn6")],
        [InlineKeyboardButton(text='Локация из Pinterest', url="https://maps.app.goo.gl/MnznPUwgC1WXBAR5A"),
         InlineKeyboardButton(text='VILLIERA WINES', url="https://maps.app.goo.gl/pfa7oucS6nxUax6X9")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_him_food_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Где позавтракать?', callback_data="routes_two_him_break"),
         InlineKeyboardButton(text='Где пообедать?', callback_data="routes_two_him_lun")],
        [InlineKeyboardButton(text='Где поужинать?', callback_data="routes_two_him_din"),
         InlineKeyboardButton(text='Кофейни', callback_data="routes_two_him_cof")],
        [InlineKeyboardButton(text='Матча', url="https://maps.app.goo.gl/RrfaL9A8K8XfevP2A?g_st=ipc"),
         InlineKeyboardButton(text='Другие напитки', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_two_him_break_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/62JZqChrsb3FsEQX6"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/aRLYobWL6oVw8fKy5")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/66Vdw179gNjWaE1e7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/DAYpbSVYSLfhLNVx6")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/S41iJ7jToucgJy9m9")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/G2e415R866JJPiNeA")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_him_lun_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/KWCkZ1GSHyU2iApw7"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/AnNPag6tXSxT5ygL6")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/Eg3fB3gbnSGhfSJE7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/dT2w62n7xiRSJKZE8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/LvJTermoWYJRrbgA6")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/PixeH7D6Ds6Vkg26A")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_two_him_din_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/iiLUYdqktAzTvRs39"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/xxeJu2S5j8B2grRd8")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/UQDFUeU6xu8BBFzQ8"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/6scpUzcBJBKTkCGX7")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/y8eEY1nRyP9gXU3x7")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/Cv8XB3HtG89kuqwv9")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_him_cof_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/8LSUddTPq63YUxHN8"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/Kmmj2C9Eop46LSUWA")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/fodhkQhguoX8jiVA7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/Yhz1LX2jxhQiD3yf8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/M6jT9MZjMnu7SZM6A")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/o8mzJmTcqhxZWA228")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_him_ani_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Информация о путеводителе', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Винодельня с сафари', url="https://maps.app.goo.gl/4Ga7RW3ejPGLdcDr8?g_st=ipc")],
        [InlineKeyboardButton(text='Ферма с Альпаками', url="https://maps.app.goo.gl/LDXMumM7o8Hakhjh7"),
         InlineKeyboardButton(text='Птицы', url="https://maps.app.goo.gl/tzfTNASyxZyc3WBz8?g_st=ipc")],
        [InlineKeyboardButton(text='Морские котики', url="https://maps.app.goo.gl/5e7SS53VpDxL5iN68?g_st=ipc"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_him_cult_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Англиканская церковь', url="https://maps.app.goo.gl/7PSarxFC344FETZJ7"),
         InlineKeyboardButton(text='Norval Foundation', url="https://maps.app.goo.gl/kgxewHb871qhJkfi7?g_st=ipc")],
        [InlineKeyboardButton(text='Музей шестого квартала', url="https://maps.app.goo.gl/TrnyhAEiCbzSFzaS7?g_st=ipc"),
         InlineKeyboardButton(text='Woodstock Exchange', url="https://maps.app.goo.gl/FhPsVXai8uc3JY2W6?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_him_ext_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_two_him_shop_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='AKJP STUDIO', url="https://maps.app.goo.gl/5hjyCXQrTKc8oBmM9"),
         InlineKeyboardButton(text='Century Blvd', url="https://maps.app.goo.gl/oXbZmN2xcQZpCqVb6")],
        [InlineKeyboardButton(text='The Old Biscuit Mill Market', url="https://maps.app.goo.gl/XECH1tm2ty7z5tv58"),
         InlineKeyboardButton(text='PICHULIK Atelier', url="https://maps.app.goo.gl/b3Vdf7Q8SYbcBced6")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ]) 

def routes_two_him_bars_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Harringtons Cocktail Lounge', url="https://maps.app.goo.gl/baGsjDtddcTiu5VR8")],
        [InlineKeyboardButton(text='Café Caprice', url="https://maps.app.goo.gl/GUei1JK1HRRmTiC79"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

               
def routes_alone_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Пешком + Такси + BUS', callback_data="routes_alone_tran"),
         InlineKeyboardButton(text='Автомобиль / мотоцикл', callback_data="routes_alone_him")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_int_ikb():
        return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Природа', callback_data="routes_alone_nat"),
         InlineKeyboardButton(text='Еда и Напитки', callback_data="routes_alone_food")],
        [InlineKeyboardButton(text='Животные', callback_data="routes_alone_ani"),
         InlineKeyboardButton(text='Культурная программа', callback_data="routes_alone_cult")],
        [InlineKeyboardButton(text='Экстрим', callback_data="routes_alone_ext"),
         InlineKeyboardButton(text='Шопинг', callback_data="routes_alone_shop")],
        [InlineKeyboardButton(text='Бары', callback_data="routes_alone_bars"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_nat_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Парк', url="https://maps.app.goo.gl/icUHS8pKQXzeN9HF8"),
         InlineKeyboardButton(text='Водопад', url="https://maps.app.goo.gl/N6ujuLYG1BUPGofn6")],
        [InlineKeyboardButton(text='Каньон реки Блайд', url="https://maps.app.goo.gl/bZjtm8cfDeps46S67"),
         InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_food_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Где позавтракать?', callback_data="routes_alone_break"),
         InlineKeyboardButton(text='Где пообедать?', callback_data="routes_alone_lun")],
        [InlineKeyboardButton(text='Где поужинать?', callback_data="routes_alone_din"),
         InlineKeyboardButton(text='Кофейни', callback_data="routes_alone_cof")],
        [InlineKeyboardButton(text='Матча', url="https://maps.app.goo.gl/RrfaL9A8K8XfevP2A?g_st=ipc"),
         InlineKeyboardButton(text='Другие напитки', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_alone_break_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/YtjFVAvhP7F26CYN6"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/aRLYobWL6oVw8fKy5")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/66Vdw179gNjWaE1e7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/DAYpbSVYSLfhLNVx6")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/S41iJ7jToucgJy9m9")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/G2e415R866JJPiNeA")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_lun_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/KWCkZ1GSHyU2iApw7"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/AnNPag6tXSxT5ygL6")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/Eg3fB3gbnSGhfSJE7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/dT2w62n7xiRSJKZE8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/LvJTermoWYJRrbgA6")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/PixeH7D6Ds6Vkg26A")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_alone_din_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/iiLUYdqktAzTvRs39"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/xxeJu2S5j8B2grRd8")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/UQDFUeU6xu8BBFzQ8"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/6scpUzcBJBKTkCGX7")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/y8eEY1nRyP9gXU3x7")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/Cv8XB3HtG89kuqwv9")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_cof_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/8LSUddTPq63YUxHN8"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/Kmmj2C9Eop46LSUWA")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/fodhkQhguoX8jiVA7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/Yhz1LX2jxhQiD3yf8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/M6jT9MZjMnu7SZM6A")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/o8mzJmTcqhxZWA228")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_ani_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Информация о путеводителе', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Винодельня с сафари', url="https://maps.app.goo.gl/4Ga7RW3ejPGLdcDr8?g_st=ipc")],
        [InlineKeyboardButton(text='Ферма с Альпаками', url="https://maps.app.goo.gl/LDXMumM7o8Hakhjh7"),
         InlineKeyboardButton(text='Птицы', url="https://maps.app.goo.gl/tzfTNASyxZyc3WBz8?g_st=ipc")],
        [InlineKeyboardButton(text='Морские котики', url="https://maps.app.goo.gl/5e7SS53VpDxL5iN68?g_st=ipc"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_cult_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Zeitz MOCAA', url="https://maps.app.goo.gl/3pqau2fVivFgTEUy6?g_st=ipc"),
         InlineKeyboardButton(text='Norval Foundation', url="https://maps.app.goo.gl/kgxewHb871qhJkfi7?g_st=ipc")],
        [InlineKeyboardButton(text='Музей шестого квартала', url="https://maps.app.goo.gl/TrnyhAEiCbzSFzaS7?g_st=ipc"),
         InlineKeyboardButton(text='Woodstock Exchange', url="https://maps.app.goo.gl/FhPsVXai8uc3JY2W6?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_ext_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_shop_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='AKJP STUDIO', url="https://maps.app.goo.gl/5hjyCXQrTKc8oBmM9"),
         InlineKeyboardButton(text='Century Blvd', url="https://maps.app.goo.gl/oXbZmN2xcQZpCqVb6")],
        [InlineKeyboardButton(text='The Old Biscuit Mill Market', url="https://maps.app.goo.gl/XECH1tm2ty7z5tv58"),
         InlineKeyboardButton(text='Vorster & Braye Ceramic Design', url="https://maps.app.goo.gl/KK632VZ4dwaRpf3G7")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ]) 

def routes_alone_bars_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Arcade | Bar & Nightlife', url="https://maps.app.goo.gl/AkZ6AD91SmRXPquZ9")],
        [InlineKeyboardButton(text='Wine Club', url="https://www.instagram.com/p/DKxDVQIi5vY/?utm_source=ig_web_copy_link"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])


def routes_alone_him_int_ikb():
        return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Природа', callback_data="routes_alone_him_nat"),
         InlineKeyboardButton(text='Еда и Напитки', callback_data="routes_alone_him_food")],
        [InlineKeyboardButton(text='Животные', callback_data="routes_alone_him_ani"),
         InlineKeyboardButton(text='Культурная программа', callback_data="routes_alone_him_cult")],
        [InlineKeyboardButton(text='Экстрим', callback_data="routes_alone_him_ext"),
         InlineKeyboardButton(text='Шопинг', callback_data="routes_alone_him_shop")],
        [InlineKeyboardButton(text='Бары', callback_data="routes_alone_him_bars"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_him_nat_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Парк', url="https://maps.app.goo.gl/icUHS8pKQXzeN9HF8"),
         InlineKeyboardButton(text='Woolley & Tidal Pool', url="https://maps.app.goo.gl/191gCkgPmhERw7M96")],
        [InlineKeyboardButton(text='Локация из Pinterest', url="https://maps.app.goo.gl/MnznPUwgC1WXBAR5A"),
         InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_him_food_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Где позавтракать?', callback_data="routes_alone_him_break"),
         InlineKeyboardButton(text='Где пообедать?', callback_data="routes_alone_him_lun")],
        [InlineKeyboardButton(text='Где поужинать?', callback_data="routes_alone_him_din"),
         InlineKeyboardButton(text='Кофейни', callback_data="routes_alone_him_cof")],
        [InlineKeyboardButton(text='Матча', url="https://maps.app.goo.gl/RrfaL9A8K8XfevP2A?g_st=ipc"),
         InlineKeyboardButton(text='Другие напитки', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_alone_him_break_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/YtjFVAvhP7F26CYN6"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/aRLYobWL6oVw8fKy5")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/66Vdw179gNjWaE1e7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/DAYpbSVYSLfhLNVx6")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/S41iJ7jToucgJy9m9")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/G2e415R866JJPiNeA")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_him_lun_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/KWCkZ1GSHyU2iApw7"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/AnNPag6tXSxT5ygL6")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/Eg3fB3gbnSGhfSJE7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/dT2w62n7xiRSJKZE8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/LvJTermoWYJRrbgA6")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/PixeH7D6Ds6Vkg26A")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_alone_him_din_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/iiLUYdqktAzTvRs39"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/xxeJu2S5j8B2grRd8")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/UQDFUeU6xu8BBFzQ8"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/6scpUzcBJBKTkCGX7")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/y8eEY1nRyP9gXU3x7")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/Cv8XB3HtG89kuqwv9")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_him_cof_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/8LSUddTPq63YUxHN8"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/Kmmj2C9Eop46LSUWA")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/fodhkQhguoX8jiVA7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/Yhz1LX2jxhQiD3yf8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/M6jT9MZjMnu7SZM6A")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/o8mzJmTcqhxZWA228")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_him_ani_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Информация о путеводителе', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Винодельня с сафари', url="https://maps.app.goo.gl/4Ga7RW3ejPGLdcDr8?g_st=ipc")],
        [InlineKeyboardButton(text='Пингвины', url="https://maps.app.goo.gl/UEJxb4cBM7FQLNrL7?g_st=ipc"),
         InlineKeyboardButton(text='Птицы', url="https://maps.app.goo.gl/tzfTNASyxZyc3WBz8?g_st=ipc")],
        [InlineKeyboardButton(text='Морские котики', url="https://maps.app.goo.gl/5e7SS53VpDxL5iN68?g_st=ipc"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_him_cult_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Franschhoek Motor Museum', url="https://maps.app.goo.gl/NnFioKyTC6eqZTL29"),
         InlineKeyboardButton(text='Norval Foundation', url="https://maps.app.goo.gl/kgxewHb871qhJkfi7?g_st=ipc")],
        [InlineKeyboardButton(text='Музей шестого квартала', url="https://maps.app.goo.gl/TrnyhAEiCbzSFzaS7?g_st=ipc"),
         InlineKeyboardButton(text='Woodstock Exchange', url="https://maps.app.goo.gl/FhPsVXai8uc3JY2W6?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Centre for the Book', url="https://maps.app.goo.gl/eG1rkL1VEKKWuTLd7")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_him_ext_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_alone_him_shop_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='AKJP STUDIO', url="https://maps.app.goo.gl/5hjyCXQrTKc8oBmM9"),
         InlineKeyboardButton(text='Century Blvd', url="https://maps.app.goo.gl/oXbZmN2xcQZpCqVb6")],
        [InlineKeyboardButton(text='The Old Biscuit Mill Market', url="https://maps.app.goo.gl/XECH1tm2ty7z5tv58"),
         InlineKeyboardButton(text='Vorster & Braye Ceramic Design', url="https://maps.app.goo.gl/KK632VZ4dwaRpf3G7")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ]) 

def routes_alone_him_bars_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Harringtons Cocktail Lounge', url="https://maps.app.goo.gl/baGsjDtddcTiu5VR8")],
        [InlineKeyboardButton(text='Café Caprice', url="https://maps.app.goo.gl/GUei1JK1HRRmTiC79"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

           
def routes_family_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Природа', callback_data="routes_fam_nat"),
         InlineKeyboardButton(text='Еда и Напитки', callback_data="routes_fam_food")],
        [InlineKeyboardButton(text='Животные', callback_data="routes_fam_ani"),
         InlineKeyboardButton(text='Культурная программа', callback_data="routes_fam_cult")],
        [InlineKeyboardButton(text='Шопинг', callback_data="routes_fam_shop"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fam_nat_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Парк', url="https://maps.app.goo.gl/icUHS8pKQXzeN9HF8"),
         InlineKeyboardButton(text='Смотровая Ложной Бухты', url="https://maps.app.goo.gl/N6ujuLYG1BUPGofn6")],
        [InlineKeyboardButton(text='Локация из Pinterest', url="https://maps.app.goo.gl/MnznPUwgC1WXBAR5A"),
         InlineKeyboardButton(text='Клифтон Вью', url="https://maps.app.goo.gl/JjaqvzB62moRUxY88?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Camps Bay Nature Park', url="https://maps.app.goo.gl/hnh7jYUQDBeVB5Gt7?g_st=ipc")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fam_food_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Где позавтракать?', callback_data="routes_fam_break"),
         InlineKeyboardButton(text='Где пообедать?', callback_data="routes_fam_lun")],
        [InlineKeyboardButton(text='Где поужинать?', callback_data="routes_fam_din"),
         InlineKeyboardButton(text='Кофейни', callback_data="routes_fam_cof")],
        [InlineKeyboardButton(text='Матча', url="https://maps.app.goo.gl/RrfaL9A8K8XfevP2A?g_st=ipc"),
         InlineKeyboardButton(text='Еще больше заведений', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_fam_break_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/YtjFVAvhP7F26CYN6"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/aRLYobWL6oVw8fKy5")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/66Vdw179gNjWaE1e7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/DAYpbSVYSLfhLNVx6")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/S41iJ7jToucgJy9m9")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/G2e415R866JJPiNeA")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fam_lun_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/KWCkZ1GSHyU2iApw7"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/AnNPag6tXSxT5ygL6")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/Eg3fB3gbnSGhfSJE7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/dT2w62n7xiRSJKZE8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/LvJTermoWYJRrbgA6")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/PixeH7D6Ds6Vkg26A")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_fam_din_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/iiLUYdqktAzTvRs39"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/xxeJu2S5j8B2grRd8")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/UQDFUeU6xu8BBFzQ8"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/6scpUzcBJBKTkCGX7")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/y8eEY1nRyP9gXU3x7")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/piBk9r3vXo2d1tvE8?g_st=ipc")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fam_cof_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/8LSUddTPq63YUxHN8"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/Kmmj2C9Eop46LSUWA")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/fodhkQhguoX8jiVA7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/Yhz1LX2jxhQiD3yf8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/M6jT9MZjMnu7SZM6A")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/o8mzJmTcqhxZWA228")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fam_ani_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Информация о путеводителе', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Винодельня с сафари', url="https://maps.app.goo.gl/4Ga7RW3ejPGLdcDr8?g_st=ipc")],
        [InlineKeyboardButton(text='Ферма с Альпаками', url="https://maps.app.goo.gl/LDXMumM7o8Hakhjh7"),
         InlineKeyboardButton(text='Птицы', url="https://maps.app.goo.gl/tzfTNASyxZyc3WBz8?g_st=ipc")],
        [InlineKeyboardButton(text='Морские котики', url="https://maps.app.goo.gl/5e7SS53VpDxL5iN68?g_st=ipc"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fam_cult_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Wonderland', url="https://maps.app.goo.gl/sUKdZ6rWwLKDYRC9A"),
         InlineKeyboardButton(text='WHATIFTHEWORLD', url="https://maps.app.goo.gl/ChFQrRDH46e1GTRdA")],
        [InlineKeyboardButton(text='Norval Foundation', url="https://maps.app.goo.gl/kgxewHb871qhJkfi7?g_st=ipc"),
         InlineKeyboardButton(text='Музей шестого квартала', url="https://maps.app.goo.gl/TrnyhAEiCbzSFzaS7?g_st=ipc")],
        [InlineKeyboardButton(text='Woodstock Exchange', url="https://maps.app.goo.gl/FhPsVXai8uc3JY2W6?g_st=ipc"),
         InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_fam_shop_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='AKJP STUDIO', url="https://maps.app.goo.gl/5hjyCXQrTKc8oBmM9"),
         InlineKeyboardButton(text='Century Blvd', url="https://maps.app.goo.gl/oXbZmN2xcQZpCqVb6")],
        [InlineKeyboardButton(text='The Old Biscuit Mill Market', url="https://maps.app.goo.gl/XECH1tm2ty7z5tv58"),
         InlineKeyboardButton(text='PICHULIK Atelier', url="https://maps.app.goo.gl/b3Vdf7Q8SYbcBced6")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ]) 

    
def routes_friends_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Пешком + Такси + BUS', callback_data="routes_fri_tran"),
         InlineKeyboardButton(text='Автомобиль / мотоцикл', callback_data="routes_fri_him")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_fri_int_ikb():
        return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Природа', callback_data="routes_fri_nat"),
         InlineKeyboardButton(text='Еда и Напитки', callback_data="routes_fri_food")],
        [InlineKeyboardButton(text='Животные', callback_data="routes_fri_ani"),
         InlineKeyboardButton(text='Культурная программа', callback_data="routes_fri_cult")],
        [InlineKeyboardButton(text='Экстрим', callback_data="routes_fri_ext"),
         InlineKeyboardButton(text='Шопинг', callback_data="routes_fri_shop")],
        [InlineKeyboardButton(text='Бары', callback_data="routes_fri_bars"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_nat_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Парк', url="https://maps.app.goo.gl/icUHS8pKQXzeN9HF8"),
         InlineKeyboardButton(text='Смотровая Ложной Бухты', url="https://maps.app.goo.gl/N6ujuLYG1BUPGofn6")],
        [InlineKeyboardButton(text='Локация из Pinterest', url="https://maps.app.goo.gl/MnznPUwgC1WXBAR5A"),
         InlineKeyboardButton(text='Muizenberg Пляж', url="https://maps.app.goo.gl/Q7isdTJAwLxnDC1S7?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Camps Bay Nature Park', url="https://maps.app.goo.gl/hnh7jYUQDBeVB5Gt7?g_st=ipc")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_food_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Где позавтракать?', callback_data="routes_fri_break"),
         InlineKeyboardButton(text='Где пообедать?', callback_data="routes_fri_lun")],
        [InlineKeyboardButton(text='Где поужинать?', callback_data="routes_fri_din"),
         InlineKeyboardButton(text='Кофейни', callback_data="routes_fri_cof")],
        [InlineKeyboardButton(text='Матча', url="https://maps.app.goo.gl/RrfaL9A8K8XfevP2A?g_st=ipc"),
         InlineKeyboardButton(text='Еще больше заведений', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_fri_break_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/YtjFVAvhP7F26CYN6"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/aRLYobWL6oVw8fKy5")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/66Vdw179gNjWaE1e7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/DAYpbSVYSLfhLNVx6")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/S41iJ7jToucgJy9m9")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/G2e415R866JJPiNeA")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_lun_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/KWCkZ1GSHyU2iApw7"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/AnNPag6tXSxT5ygL6")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/Eg3fB3gbnSGhfSJE7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/dT2w62n7xiRSJKZE8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/LvJTermoWYJRrbgA6")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/PixeH7D6Ds6Vkg26A")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_fri_din_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/iiLUYdqktAzTvRs39"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/xxeJu2S5j8B2grRd8")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/UQDFUeU6xu8BBFzQ8"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/6scpUzcBJBKTkCGX7")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/y8eEY1nRyP9gXU3x7")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/piBk9r3vXo2d1tvE8?g_st=ipc")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_cof_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/8LSUddTPq63YUxHN8"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/Kmmj2C9Eop46LSUWA")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/fodhkQhguoX8jiVA7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/Yhz1LX2jxhQiD3yf8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/M6jT9MZjMnu7SZM6A")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/o8mzJmTcqhxZWA228")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_ani_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Информация о путеводителе', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Винодельня с сафари', url="https://maps.app.goo.gl/4Ga7RW3ejPGLdcDr8?g_st=ipc")],
        [InlineKeyboardButton(text='Ферма с Альпаками', url="https://maps.app.goo.gl/LDXMumM7o8Hakhjh7"),
         InlineKeyboardButton(text='Птицы', url="https://maps.app.goo.gl/tzfTNASyxZyc3WBz8?g_st=ipc")],
        [InlineKeyboardButton(text='Морские котики', url="https://maps.app.goo.gl/5e7SS53VpDxL5iN68?g_st=ipc"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_cult_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='WHATIFTHEWORLD', url="https://maps.app.goo.gl/ChFQrRDH46e1GTRdA"),
         InlineKeyboardButton(text='Norval Foundation', url="https://maps.app.goo.gl/kgxewHb871qhJkfi7?g_st=ipc")],
        [InlineKeyboardButton(text='Музей шестого квартала', url="https://maps.app.goo.gl/TrnyhAEiCbzSFzaS7?g_st=ipc"),
         InlineKeyboardButton(text='Woodstock Exchange', url="https://maps.app.goo.gl/FhPsVXai8uc3JY2W6?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_ext_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Ceres Zipline Adventures', url="https://maps.app.goo.gl/NdjKJSM7poknG3x87")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_shop_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='AKJP STUDIO', url="https://maps.app.goo.gl/5hjyCXQrTKc8oBmM9"),
         InlineKeyboardButton(text='Century Blvd', url="https://maps.app.goo.gl/oXbZmN2xcQZpCqVb6")],
        [InlineKeyboardButton(text='The Old Biscuit Mill Market', url="https://maps.app.goo.gl/XECH1tm2ty7z5tv58"),
         InlineKeyboardButton(text='PICHULIK Atelier', url="https://maps.app.goo.gl/b3Vdf7Q8SYbcBced6")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ]) 

def routes_fri_bars_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='ASOKA BAR', url="https://maps.app.goo.gl/V55PwnYXWiKTMm1LA")],
        [InlineKeyboardButton(text='THE ATHLETIC', url="https://maps.app.goo.gl/Li2YZRtGupVheY2y8"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])


def routes_fri_him_int_ikb():
        return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Природа', callback_data="routes_fri_him_nat"),
         InlineKeyboardButton(text='Еда и Напитки', callback_data="routes_fri_him_food")],
        [InlineKeyboardButton(text='Животные', callback_data="routes_fri_him_ani"),
         InlineKeyboardButton(text='Культурная программа', callback_data="routes_fri_him_cult")],
        [InlineKeyboardButton(text='Экстрим', callback_data="routes_fri_him_ext"),
         InlineKeyboardButton(text='Шопинг', callback_data="routes_fri_him_shop")],
        [InlineKeyboardButton(text='Бары', callback_data="routes_fri_him_bars"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_him_nat_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Парк', url="https://maps.app.goo.gl/icUHS8pKQXzeN9HF8"),
         InlineKeyboardButton(text='Смотровая Ложной Бухты', url="https://maps.app.goo.gl/N6ujuLYG1BUPGofn6")],
        [InlineKeyboardButton(text='Локация из Pinterest', url="https://maps.app.goo.gl/MnznPUwgC1WXBAR5A"),
         InlineKeyboardButton(text='Клифтон Вью', url="https://maps.app.goo.gl/JjaqvzB62moRUxY88?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Camps Bay Nature Park', url="https://maps.app.goo.gl/hnh7jYUQDBeVB5Gt7?g_st=ipc")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_him_food_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Где позавтракать?', callback_data="routes_two_him_break"),
         InlineKeyboardButton(text='Где пообедать?', callback_data="routes_two_him_lun")],
        [InlineKeyboardButton(text='Где поужинать?', callback_data="routes_two_him_din"),
         InlineKeyboardButton(text='Кофейни', callback_data="routes_two_him_cof")],
        [InlineKeyboardButton(text='Матча', url="https://maps.app.goo.gl/RrfaL9A8K8XfevP2A?g_st=ipc"),
         InlineKeyboardButton(text='Еще больше заведений', url="https://t.me/tribute/app?startapp=peKg")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_fri_him_break_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/YtjFVAvhP7F26CYN6"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/aRLYobWL6oVw8fKy5")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/66Vdw179gNjWaE1e7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/DAYpbSVYSLfhLNVx6")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/S41iJ7jToucgJy9m9")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/G2e415R866JJPiNeA")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_him_lun_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/KWCkZ1GSHyU2iApw7"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/AnNPag6tXSxT5ygL6")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/Eg3fB3gbnSGhfSJE7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/dT2w62n7xiRSJKZE8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/LvJTermoWYJRrbgA6")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/PixeH7D6Ds6Vkg26A")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def routes_fri_him_din_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/iiLUYdqktAzTvRs39"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/xxeJu2S5j8B2grRd8")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/UQDFUeU6xu8BBFzQ8"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/6scpUzcBJBKTkCGX7")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/y8eEY1nRyP9gXU3x7")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/piBk9r3vXo2d1tvE8?g_st=ipc")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_him_cof_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Центр/City Bowl', url="https://maps.app.goo.gl/8LSUddTPq63YUxHN8"),
         InlineKeyboardButton(text='🎨 Woodstock', url="https://maps.app.goo.gl/Kmmj2C9Eop46LSUWA")],
        [InlineKeyboardButton(text='🏄‍♂️ Muizenberg & Kalk Bay', url="https://maps.app.goo.gl/fodhkQhguoX8jiVA7"),
         InlineKeyboardButton(text='🚗 За городом', url="https://maps.app.goo.gl/Yhz1LX2jxhQiD3yf8")],
        [InlineKeyboardButton(text='🌊 Атлантическое побережье (Sea Point/Camps Bay)', url="https://maps.app.goo.gl/M6jT9MZjMnu7SZM6A")],
        [InlineKeyboardButton(text='🍷 Constantia & Южные фермы', url="https://maps.app.goo.gl/o8mzJmTcqhxZWA228")],
        [InlineKeyboardButton(text='Больше мест', url="https://t.me/+evy3wj86wl9lN2Ey"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_him_ani_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Информация о путеводителе', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Винодельня с сафари', url="https://maps.app.goo.gl/4Ga7RW3ejPGLdcDr8?g_st=ipc")],
        [InlineKeyboardButton(text='Ферма с Альпаками', url="https://maps.app.goo.gl/LDXMumM7o8Hakhjh7"),
         InlineKeyboardButton(text='Птицы', url="https://maps.app.goo.gl/tzfTNASyxZyc3WBz8?g_st=ipc")],
        [InlineKeyboardButton(text='Морские котики', url="https://maps.app.goo.gl/5e7SS53VpDxL5iN68?g_st=ipc"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_him_cult_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='WHATIFTHEWORLD', url="https://maps.app.goo.gl/ChFQrRDH46e1GTRdA"),
         InlineKeyboardButton(text='Norval Foundation', url="https://maps.app.goo.gl/kgxewHb871qhJkfi7?g_st=ipc")],
        [InlineKeyboardButton(text='Музей шестого квартала', url="https://maps.app.goo.gl/TrnyhAEiCbzSFzaS7?g_st=ipc"),
         InlineKeyboardButton(text='Woodstock Exchange', url="https://maps.app.goo.gl/FhPsVXai8uc3JY2W6?g_st=ipc")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_him_ext_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='Ceres Zipline Adventures', url="https://maps.app.goo.gl/NdjKJSM7poknG3x87")],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])

def routes_fri_him_shop_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='AKJP STUDIO', url="https://maps.app.goo.gl/5hjyCXQrTKc8oBmM9"),
         InlineKeyboardButton(text='Century Blvd', url="https://maps.app.goo.gl/oXbZmN2xcQZpCqVb6")],
        [InlineKeyboardButton(text='The Old Biscuit Mill Market', url="https://maps.app.goo.gl/XECH1tm2ty7z5tv58"),
         InlineKeyboardButton(text='PICHULIK Atelier', url="https://maps.app.goo.gl/b3Vdf7Q8SYbcBced6")],
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ]) 


def routes_fri_him_bars_ikb():
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Путеводитель', url="https://t.me/tribute/app?startapp=peKg"),
         InlineKeyboardButton(text='ASOKA BAR', url="https://maps.app.goo.gl/V55PwnYXWiKTMm1LA")],
        [InlineKeyboardButton(text='THE ATHLETIC', url="https://maps.app.goo.gl/Li2YZRtGupVheY2y8"),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
