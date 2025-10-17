import logging
from aiogram import Router, types, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import Config
from db import Database
from keyboards.inline import housing_menu_ikb, housing_rent_ikb, housing_request_ikb, back_start_menu

router = Router()
db = Database()

class HousingStates(StatesGroup):
    waiting_for_housing_data = State() 

@router.callback_query(F.data == 'housing')
async def housing_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🏠 Только свежие и реальные объявления.\n"
        "📅 Каждое объявление активно 14 дней, потом его нужно обновить.\n"
        "Здесь вы сможете:\n"
        "— найти квартиру, комнату или дом\n"
        "— разместить своё объявление\n"
        "Что интересует?\n",
        reply_markup=housing_menu_ikb(),
        parse_mode="HTML")
    
@router.callback_query(F.data == 'housing_rent')
async def housing_rent(callback: types.CallbackQuery):
    text_template = "Приветсвую я из Bro BOT пишу по теме недвижимости, мне нужна консультация\n\nНа тему: Сопровождение покупка/продажа, аренда коммерческого помещения, аренда от 6 месяцев и больше\n"
    
    await callback.message.edit_text(
        "Скопируйте шаблон и отправляйте @controllinginternational\n\n"
        "<code>Приветсвую я из Bro BOT пишу по теме недвижимости, мне нужна консультация\n\n"
        "На тему: Сопровождение покупка/продажа, аренда коммерческого помещения, аренда от 6 месяцев и больше\n</code>",
        reply_markup=housing_rent_ikb(text_template),
        parse_mode="HTML")
    
@router.callback_query(F.data == 'housing_rent')
async def housing_rent(callback: types.CallbackQuery):
    text_template = """
Приветсвую я из Bro BOT пишу по теме недвижимости, мне нужна консультация

На тему: Сопровождение покупка/продажа, аренда коммерческого помещения, аренда от 6 месяцев и больше"""
    
    await callback.message.edit_text(
        "Скопируйте шаблон и отправляйте @controllinginternational\n\n"
        "<code>Приветсвую я из Bro BOT пишу по теме недвижимости, мне нужна консультация\n\n"
        "На тему: Сопровождение покупка/продажа, аренда коммерческого помещения, аренда от 6 месяцев и больше\n</code>",
        reply_markup=housing_rent_ikb(text_template),
        parse_mode="HTML")
    
@router.callback_query(F.data == 'housing_request')
async def housing_request(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(HousingStates.waiting_for_housing_data)
    
    contact = f"@{callback.from_user.username}" if callback.from_user.username else ""
    
    search_template = f"""
<b>Шаблон: Ищу недвижимость</b>
<code><b>📍 Район:</b>
<b>🏠 Тип жилья (квартира / вилла / комната / студия):</b>
<b>💰 Цена (в ZAR / USD / ₽):</b> 
<b>📅 Срок аренды (посут. / долгоср.):</b>
<b>🧾 Короткое описание о себе:</b>
<b>👤 Контакт (TG ник или телефон):</b> {contact}</code>"""

    rent_template = f"""
<b>Шаблон: Сдаю недвижимость</b>
<code><b>📍 Район / Локация:</b>
<b>🏠 Тип жилья (квартира / вилла / комната):</b>
<b>💰 Цена (в ZAR / USD / ₽, укажи за день или месяц):</b> 
<b>📅 Срок аренды (посут. / долгоср. / минимальный срок):</b>
<b>🧾 Короткое описание (до 250 символов — интерьер, удобства, расстояние до моря и т.д.):</b>
<b>👤 Контакт (TG ник или телефон):</b> {contact}</code>
📸 По желанию прикрепите фото"""

    sail_template = f"""
<b>Шаблон: Продаю недвижимость</b>
<code><b>📍 Район / Локация:</b>
<b>🏠 Тип жилья (квартира / студия / комната / дом):</b>
<b>💰 Цена (в ZAR / USD / ₽, укажи за день или месяц):</b> 
<b>📅 Срок аренды (посут. / долгоср.):</b>
<b>🧾 Короткое описание (до 250 символов — интерьер, удобства, расстояние до моря и т.д.):</b>
<b>👤 Контакт (TG ник или телефон):</b> {contact}</code>
📸 По желанию прикрепите фото"""
    
    await callback.message.edit_text(
        "Скопируйте нужный шаблон, заполните его и отправьте боту в ответ. Обьявление пройдет модерацию и вскоре будет опубликовано на 14 дней, после чего вы получите уведомление.\n"
        f"{search_template}\n"
        f"{rent_template}\n"
        f"{sail_template}\n",
        reply_markup=housing_request_ikb(),
        parse_mode="HTML")
    
# Обработчик текстового сообщения с данными мероприятия
@router.message(HousingStates.waiting_for_housing_data, F.text)
async def process_housing_data(message: types.Message, state: FSMContext, bot: Bot):
    housing_data = message.text
    user = message.from_user
    
    # Добавляем/обновляем пользователя в БД
    db.add_user(
        tg_id=user.id,
        username=user.username,
        full_name=user.full_name
    )
    
    # Получаем пользователя из БД для получения ID
    user_db = db.get_user(user.id)
    
    if user_db:
        # Сохраняем заявку в БД с выбранной длительностью
        request_id = db.add_request(
            user_id=user_db['id'],
            request_type='housing',
            text=housing_data,
            duration_days=14  # Добавляем длительность
        )
        
        if request_id:
            # Отправляем уведомление админам
            await notify_admins_about_new_housing(bot, housing_data, user, request_id)
            
            # Уведомляем пользователя
            await message.answer(
                f"✅ Спасибо! Ваше объявление получено и отправлено на модерацию.\n"
                f"Длительность размещения: 14 дней\n"
                f"Мы проверим его и добавим в афишу в течение 24 часов.",
                reply_markup=back_start_menu()
            )
        else:
            await message.answer(
                "❌ Произошла ошибка при сохранении объявления. Попробуйте позже.",
                reply_markup=back_start_menu()
            )
    else:
        await message.answer(
            "❌ Ошибка при обработке вашего запроса. Попробуйте позже.",
            reply_markup=back_start_menu()
        )
    
    # Сбрасываем состояние
    await state.clear()

# Обработчик для медиа-сообщений (фото с подписью)
@router.message(HousingStates.waiting_for_housing_data, F.photo)
async def process_housing_data_with_photo(message: types.Message, state: FSMContext, bot: Bot):
    user = message.from_user
    
    if message.caption:
        housing_data = message.caption
        photo_id = message.photo[-1].file_id
        
        # Добавляем/обновляем пользователя в БД
        db.add_user(
            tg_id=user.id,
            username=user.username,
            full_name=user.full_name
        )
        
        # Получаем пользователя из БД для получения ID
        user_db = db.get_user(user.id)
        
        if user_db:
            # Сохраняем заявку в БД с путями к медиа и длительностью
            request_id = db.add_request(
                user_id=user_db['id'],
                request_type='housing',
                text=housing_data,
                media_paths=[photo_id],  # Сохраняем file_id фото
                duration_days=14
            )
            
            if request_id:
                # Отправляем уведомление админам с фото
                await notify_admins_about_new_housing_with_photo(bot, housing_data, user, request_id, photo_id)
                
                await message.answer(
                    f"✅ Спасибо! Ваше объявление с фото получено и отправлено на модерацию.\n"
                    f"Длительность размещения: 14 дней",
                    reply_markup=back_start_menu()
                )
            else:
                await message.answer(
                    "❌ Произошла ошибка при сохранении объявления. Попробуйте позже.",
                    reply_markup=back_start_menu()
                )
        else:
            await message.answer(
                "❌ Ошибка при обработке вашего запроса. Попробуйте позже.",
                reply_markup=back_start_menu()
            )
        
    else:
        await message.answer(
            "❌ Пожалуйста, добавьте описание мероприятия к фото используя шаблон."
        )
        return 
    
    await state.clear()

async def notify_admins_about_new_housing(bot: Bot, housing_data: str, user: types.User, request_id: int):
    """Уведомляет админов о новом мероприятии (текст)"""
    try:
        
        admin_text = (
            "🎉 <b>НОВОЕ ОБЪЯВЛЕНИЕ НА МОДЕРАЦИЮ</b>\n\n"
            f"👤 <b>От:</b> {user.full_name}\n"
            f"📱 <b>Username:</b> @{user.username if user.username else 'нет'}\n"
            f"🆔 <b>User ID:</b> {user.id}\n"
            f"📋 <b>ID заявки:</b> #{request_id}\n"
            f"📅 <b>Длительность:</b> 14 дней\n\n"
            f"📝 <b>Описание мероприятия:</b>\n<code>{housing_data}</code>\n\n"
            "⚡ <i>Для обработки используйте команду /admin</i>"
        )
        
        # Отправляем всем админам
        for admin_id in Config.ADMIN_IDS:
            try:
                await bot.send_message(
                    chat_id=admin_id,
                    text=admin_text,
                    parse_mode="HTML"
                )
            except Exception as e:
                logging.error(f"Ошибка отправки админу {admin_id}: {e}")
                
    except Exception as e:
        logging.error(f"Ошибка в notify_admins_about_new_housing: {e}")

async def notify_admins_about_new_housing_with_photo(bot: Bot, housing_data: str, user: types.User, request_id: int, photo_id: str):
    """Уведомляет админов о новом мероприятии (фото + текст)"""
    try:
        
        caption = (
            "🎉 <b>НОВОЕ ОБЪЯВЛЕНИЕ НА МОДЕРАЦИЮ</b>\n\n"
            f"👤 <b>От:</b> {user.full_name}\n"
            f"📱 <b>Username:</b> @{user.username if user.username else 'нет'}\n"
            f"🆔 <b>User ID:</b> {user.id}\n"
            f"📋 <b>ID заявки:</b> #{request_id}\n"
            f"📅 <b>Длительность:</b> 14 дней\n\n"
            f"📝 <b>Описание мероприятия:</b>\n<code>{housing_data}</code>\n\n"
            "⚡ <i>Для обработки используйте команду /admin</i>"
        )
        
        # Отправляем всем админам
        for admin_id in Config.ADMIN_IDS:
            try:
                await bot.send_photo(
                    chat_id=admin_id,
                    photo=photo_id,
                    caption=caption,
                    parse_mode="HTML"
                )
            except Exception as e:
                logging.error(f"Ошибка отправки фото админу {admin_id}: {e}")
                
    except Exception as e:
        logging.error(f"Ошибка в notify_admins_about_new_housing_with_photo: {e}")