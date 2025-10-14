from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_start_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
         [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
       
    
def start_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Афиша событий', callback_data='events'),
         InlineKeyboardButton(text='Конструктор маршрута', callback_data='routes')],
        [InlineKeyboardButton(text='Жилье и недвижимость', callback_data='housing'),
         InlineKeyboardButton(text='Транспорт и аренда', callback_data='transportRent')],
        [InlineKeyboardButton(text='Объявления и услуги', callback_data='adsServices'),
         InlineKeyboardButton(text='Полезные контакты и поддержка', callback_data='contacts')]
    ])
    
def events_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Афиша месяца', callback_data='events_month'),
         InlineKeyboardButton(text='🎤 Добавить свое мероприятие', callback_data='events_request')],
        [InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def events_month_menu(pin_url):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📅 События этой недели', url=pin_url),
         InlineKeyboardButton(text='🗓 Мероприятия месяца', url='https://t.me/capetown_uar/978')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='events'),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])
    
def events_month_request():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Хочу в афишу на месяц', callback_data='events_month_request_chat')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='events'),
         InlineKeyboardButton(text='🔙 В главное меню', callback_data='start')]
    ])