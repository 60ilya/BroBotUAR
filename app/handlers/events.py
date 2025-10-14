import logging
from aiogram import Router, types, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import Config
from db import Database
from keyboards.inline import events_menu, events_month_menu, events_month_request, back_start_menu, events_month_request

router = Router()
db = Database()

class EventStates(StatesGroup):
    waiting_for_event_data = State() 

@router.callback_query(F.data == 'events')
async def cmd_start(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🎟 Всё самое интересное в Кейптауне — концерты, маркеты, вечеринки, выставки",
        reply_markup=events_menu(),
        parse_mode="HTML")
    
@router.callback_query(F.data == 'events_month')
async def events_month(callback: types.CallbackQuery, bot: Bot):
    channel_username = "@capetown_uar"
    pin_url = await get_pinned_message_url(bot, channel_username)
    
    await callback.message.edit_text(
        "🎟 <b>Афиша Кейптауна — всё самое интересное этого месяца!</b>\n"
        "🌴 Фестивали, вечеринки, маркеты, выставки, концерты и новые места — я собираю для тебя всё, что стоит внимания.\n\n"
        "💡 <b>События этой недели</b> обновляется каждую неделю, чтобы всегда быть в курсе,"
        " <b>куда пойти в выходные, где поесть вкусно, а где потанцевать до утра.</b>",
        reply_markup=events_month_menu(pin_url),
        parse_mode="HTML")
    
async def get_pinned_message_url(bot: Bot, channel_username: str) -> str:
    """Получает ссылку на закрепленное сообщение канала"""
    try:
        # Получаем информацию о канале
        chat = await bot.get_chat(channel_username)
        
        if chat.pinned_message:
            username = channel_username.lstrip('@')
            message_id = chat.pinned_message.message_id
            return f"https://t.me/{username}/{message_id}"
        else:
            return f"https://t.me/{channel_username.lstrip('@')}"
            
    except Exception as e:
        return f"Ошибка: {e}"
    
@router.callback_query(F.data == 'events_request')
async def events_request(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(EventStates.waiting_for_event_data)
    
    # Инициализируем состояние с выбором длительности по умолчанию
    await state.update_data(duration_days=14, is_monthly=False)

    await callback.message.edit_text(
        "🎉 Классно! Расскажите о своём мероприятии, и я добавлю его в События этой недели 🙌\n\n"
        "📅 <b>Выберите длительность размещения:</b>\n"
        "• Афиша недели - 14 дней (бесплатно)\n"
        "• Афиша месяца - 30 дней (за донат)\n\n"
        "Просто кликните на текст ниже, шаблон скопируется, заполните его и вышлите в ответ:\n\n"
        "<code>📍<b>Название / формат:</b> \n"
        "(пример: Sunset Jazz Party / Маркет выходного дня)\n"
        "📅 <b>Дата и время:</b> \n"
        "(пример: 25 октября, с 17:00 до 23:00)\n"
        "📍 <b>Локация:</b> \n" 
        "(название, район или ссылка на карту)\n"
        "💰 <b>Стоимость (если есть):</b> \n"
        "🧾 <b>Описание:</b> \n"
        "(2–3 предложения: что будет, для кого, чем интересно)</code>\n\n"
        "📸 (по желанию) прикрепи афишу или 1 фото\n\n"
        "💬 После модерации событие появится в афише, а я отмечу Вас как организатора\n\n"
        "🔥 События обновляется каждую неделю, разместить мероприятие можно 1 раз в 14 дней",
        reply_markup=events_month_request(is_monthly=False),
        parse_mode="HTML"
    )
    await callback.answer()

# Обработчики для toggle кнопок
@router.callback_query(F.data == 'events_duration')
async def handle_toggle_duration(callback: types.CallbackQuery, state: FSMContext):
    # Получаем текущее состояние
    state_data = await state.get_data()
    current_is_monthly = state_data.get('is_monthly', False)
    
    # Переключаем состояние
    new_is_monthly = not current_is_monthly
    duration_days = 30 if new_is_monthly else 14
    
    # Обновляем состояние
    await state.update_data(duration_days=duration_days, is_monthly=new_is_monthly)
    
    # Обновляем сообщение с новой клавиатурой
    await callback.message.edit_reply_markup(
        reply_markup=events_month_request(is_monthly=new_is_monthly)
    )
    
    # Показываем подсказку о изменении
    duration_text = "30 дней (Афиша месяца)" if new_is_monthly else "14 дней (Афиша недели)"
    await callback.answer(f"Установлена длительность: {duration_text}")
    
# Обработчик текстового сообщения с данными мероприятия
@router.message(EventStates.waiting_for_event_data, F.text)
async def process_event_data(message: types.Message, state: FSMContext, bot: Bot):
    event_data = message.text
    user = message.from_user
    
    # Получаем данные из состояния (включая duration_days)
    state_data = await state.get_data()
    duration_days = state_data.get('duration_days', 14)
    
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
            request_type='event',
            text=event_data,
            duration_days=duration_days  # Добавляем длительность
        )
        
        if request_id:
            # Отправляем уведомление админам
            await notify_admins_about_new_event(bot, event_data, user, request_id, duration_days)
            
            # Уведомляем пользователя
            duration_text = "14 дней" if duration_days == 14 else "30 дней"
            await message.answer(
                f"✅ Спасибо! Ваше мероприятие получено и отправлено на модерацию.\n"
                f"Длительность размещения: {duration_text}\n"
                f"Мы проверим его и добавим в афишу в течение 24 часов.",
                reply_markup=back_start_menu()
            )
        else:
            await message.answer(
                "❌ Произошла ошибка при сохранении мероприятия. Попробуйте позже.",
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
@router.message(EventStates.waiting_for_event_data, F.photo)
async def process_event_data_with_photo(message: types.Message, state: FSMContext, bot: Bot):
    user = message.from_user
    
    if message.caption:
        event_data = message.caption
        photo_id = message.photo[-1].file_id
        
        # Получаем данные из состояния (включая duration_days)
        state_data = await state.get_data()
        duration_days = state_data.get('duration_days', 14)
        
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
                request_type='event',
                text=event_data,
                media_paths=[photo_id],  # Сохраняем file_id фото
                duration_days=duration_days  # Добавляем длительность
            )
            
            if request_id:
                # Отправляем уведомление админам с фото
                await notify_admins_about_new_event_with_photo(bot, event_data, user, request_id, photo_id, duration_days)
                
                duration_text = "14 дней" if duration_days == 14 else "30 дней"
                await message.answer(
                    f"✅ Спасибо! Ваше мероприятие с фото получено и отправлено на модерацию.\n"
                    f"Длительность размещения: {duration_text}",
                    reply_markup=back_start_menu()
                )
            else:
                await message.answer(
                    "❌ Произошла ошибка при сохранении мероприятия. Попробуйте позже.",
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

async def notify_admins_about_new_event(bot: Bot, event_data: str, user: types.User, request_id: int, duration_days: int):
    """Уведомляет админов о новом мероприятии (текст)"""
    try:
        duration_text = "14 дней (Афиша недели)" if duration_days == 14 else "30 дней (Афиша месяца)"
        
        admin_text = (
            "🎉 <b>НОВОЕ МЕРОПРИЯТИЕ НА МОДЕРАЦИЮ</b>\n\n"
            f"👤 <b>От:</b> {user.full_name}\n"
            f"📱 <b>Username:</b> @{user.username if user.username else 'нет'}\n"
            f"🆔 <b>User ID:</b> {user.id}\n"
            f"📋 <b>ID заявки:</b> #{request_id}\n"
            f"📅 <b>Длительность:</b> {duration_text}\n\n"
            f"📝 <b>Описание мероприятия:</b>\n<code>{event_data}</code>\n\n"
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
        logging.error(f"Ошибка в notify_admins_about_new_event: {e}")

async def notify_admins_about_new_event_with_photo(bot: Bot, event_data: str, user: types.User, request_id: int, photo_id: str, duration_days: int):
    """Уведомляет админов о новом мероприятии (фото + текст)"""
    try:
        duration_text = "14 дней (Афиша недели)" if duration_days == 14 else "30 дней (Афиша месяца)"
        
        caption = (
            "🎉 <b>НОВОЕ МЕРОПРИЯТИЕ НА МОДЕРАЦИЮ</b>\n\n"
            f"👤 <b>От:</b> {user.full_name}\n"
            f"📱 <b>Username:</b> @{user.username if user.username else 'нет'}\n"
            f"🆔 <b>User ID:</b> {user.id}\n"
            f"📋 <b>ID заявки:</b> #{request_id}\n"
            f"📅 <b>Длительность:</b> {duration_text}\n\n"
            f"📝 <b>Описание мероприятия:</b>\n<code>{event_data}</code>\n\n"
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
        logging.error(f"Ошибка в notify_admins_about_new_event_with_photo: {e}")