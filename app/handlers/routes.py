import logging
from aiogram import Router, types, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import Config
from db import Database
from keyboards.inline import routes_menu

router = Router()
db = Database()


@router.callback_query(F.data == 'routes')
async def routes(callback: types.CallbackQuery):
    if db.get_user(callback.from_user.id)['notifications']:
        notification_toggle = True
    else:
        notification_toggle = False

    await callback.message.edit_text(
        "🚧 Раздел “Конструктор маршрута” пока в разработке!\n"
        "Совсем скоро Вы сможете бесплатно собрать персональный маршрут по Кейптауну — по интересам, транспорту и настроению 🌴\n"
        "Хочешь узнать, когда он запустится первым?\n\n"
        "👉 <b>Подпишись на уведомления</b> от Бро Бота",
        reply_markup=routes_menu(notification_toggle),
        parse_mode="HTML")
    
@router.callback_query(F.data == 'routes_notification')
async def routes_notification(callback: types.CallbackQuery):
    try:
        db.set_user_notification(True)
        
        await callback.message.edit_reply_markup(
            reply_markup=routes_menu(True),
            parse_mode="HTML")
    except:
        await callback.answer("Вами будет получено уведомление об открытии раздела!")
        
