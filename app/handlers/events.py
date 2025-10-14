from aiogram import Router, types, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards.inline import events_menu, events_month_menu, events_month_request, back_start_menu

router = Router()

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

    await callback.message.edit_text(
        "🎉 Классно! Расскажите о своём мероприятии, и я добавлю его в События этой недели 🙌\n\n"
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
        "🔥 События обновляется каждую неделю, разместить мероприятие можно 1 раз в 14 дней\n\n"
        "В <b>Афишу месяца</b> добавляются мероприятия за донат в Bro Bot",
        reply_markup=events_month_request(),
        parse_mode="HTML")
    
# Обработчик текстового сообщения с данными мероприятия
@router.message(EventStates.waiting_for_event_data, F.text)
async def process_event_data(message: types.Message, state: FSMContext):
    event_data = message.text
    
    # Сохраняем данные в состоянии (опционально)
    await state.update_data(event_data=event_data, user_id=message.from_user.id)
    
    # Здесь обрабатываем полученные данные
    # Например, сохраняем в БД, отправляем админу и т.д.
    
    # Уведомляем пользователя
    await message.answer(
        "✅ Спасибо! Ваше мероприятие получено и отправлено на модерацию.\n"
        "Мы проверим его и добавим в афишу в течение 24 часов.",
        reply_markup=back_start_menu()
    )
    
    # Сбрасываем состояние
    await state.clear()
    

# Обработчик для медиа-сообщений (фото с подписью)
@router.message(EventStates.waiting_for_event_data, F.photo)
async def process_event_data_with_photo(message: types.Message, state: FSMContext):
    if message.caption:
        event_data = message.caption
        photo_id = message.photo[-1].file_id
        
        await state.update_data(
            event_data=event_data, 
            user_id=message.from_user.id,
            photo_id=photo_id
        )
        
        await message.answer(
            "✅ Спасибо! Ваше мероприятие с фото получено и отправлено на модерацию.",
            reply_markup=back_start_menu()
        )

        
    else:
        await message.answer(
            "❌ Пожалуйста, добавьте описание мероприятия к фото используя шаблон."
        )
        return  # Не сбрасываем состояние, ждем правильный ввод
    
    await state.clear()