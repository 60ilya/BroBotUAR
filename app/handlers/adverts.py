import logging
from aiogram import Router, types, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from config import Config
from db import Database
from keyboards.inline import adverts_menu_ikb, adverts_request_ikb, back_start_menu

router = Router()
db = Database()

class AdvertsStates(StatesGroup):
    waiting_for_adverts_data = State() 

@router.callback_query(F.data == 'adverts')
async def adverts_menu(callback: types.CallbackQuery):
    text = """
<b>Раздел для тех, кто ищет или предлагает услуги в Кейптауне, например:</b>

🌍 <b>гиды</b> и авторские туры
📸 <b>фотографы</b>
🧘‍♀️ <b>йога</b>, ретриты и воркшопы
🥾 <b>хайки</b> и активный отдых
🎨 <b>мероприятия</b> и мастер-классы
👾 <b>услуги строители</b>, водители, няни и другое

Можно как <b>найти нужную услугу</b>, так и <b>разместить свою</b>

Все объявления действуют 14 дней, чтобы информация оставалась актуальной ✨
"""

    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_photo(
            photo=FSInputFile('app/content/menu_adverts.jpg'),
            caption=text,
            reply_markup=adverts_menu_ikb(),
            parse_mode="HTML"
        )

    
  
@router.callback_query(F.data == 'adverts_request')
async def adverts_request(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()
    except:
        pass
    
    request = db.check_recent_request_by_tg_id(
        tg_id=callback.from_user.id, 
        request_type="adverts"
    )    
    
    if request['exists']:
        await callback.message.answer(
            f"Вы уже отправляли заявку за эти 2 недели. Следующую заявку вы сможете подать через {request['time_remaining']}",
            reply_markup=adverts_request_ikb(),
            parse_mode="HTML")
        return
    
    await state.set_state(AdvertsStates.waiting_for_adverts_data)
    
    contact = f"@{callback.from_user.username}" if callback.from_user.username else ""
    
    text = f"""
✨ Классно, что хочешь рассказать о своей услуге или активности!

Здесь можно разместить информацию о турах, фотосессиях, йоге, хайках, мастер-классах и любых других полезных вещах для гостей и жителей Кейптауна 🌴

💡 Объявления публикуются на 14 дней (потом можно обновить или продлить).
Скопируй, заполни шаблон ниже и вышли мне в ответ 

<code>🧾 Название услуги / активности: (пример: Индивидуальный тур на Столовую гору / Фотосессия на пляже Кэмпс-Бэй)
💬 Короткое описание: (2–3 предложения — что вы предлагаете, чем уникально)
📍 Локация / район: (пример: Sea Point / Clifton / Центр)
💰 Стоимость или диапазон цен: (по желанию)
👤 Контакт: {contact}</code>
📸 (по желанию) прикрепи 1 фото

После модерации объявление появится в разделе “Услуги и активности” и будет видно всем пользователям 💬"""

    
    await callback.message.answer(
        text=text,
        reply_markup=adverts_request_ikb(),
        parse_mode="HTML")
    
# @router.callback_query(F.data == 'adverts_share')
# async def adverts_request(callback: types.CallbackQuery, state: FSMContext):
#     try:
#         await callback.message.delete()
#     except:
#         pass
    
#     await state.set_state(AdvertsStates.waiting_for_adverts_data)
    
#     text = f"""✨ Опишите свой запрос и мы опубликуем в недвижимость или в объявления"""

    
#     await callback.message.answer(
#         text=text,
#         reply_markup=adverts_request_ikb(),
#         parse_mode="HTML")
    
# Обработчик текстового сообщения с данными мероприятия
@router.message(AdvertsStates.waiting_for_adverts_data, F.text)
async def process_adverts_data(message: types.Message, state: FSMContext, bot: Bot):
    adverts_data = message.text
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
            request_type='adverts',
            text=adverts_data,
            duration_days=14  # Добавляем длительность
        )
        
        if request_id:
            # Отправляем уведомление админам
            await notify_admins_about_new_adverts(bot, adverts_data, user, request_id)
            
            # Уведомляем пользователя
            await message.answer(
                f"✅ Спасибо! Ваше объявление получено и отправлено на модерацию.\n"
                f"Длительность размещения: 14 дней\n"
                f"Мы проверим его и добавим в объявления в течение 24 часов.",
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
@router.message(AdvertsStates.waiting_for_adverts_data, F.photo)
async def process_adverts_data_with_photo(message: types.Message, state: FSMContext, bot: Bot):
    user = message.from_user
    
    if message.caption:
        adverts_data = message.caption
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
                request_type='adverts',
                text=adverts_data,
                media_paths=[photo_id],  # Сохраняем file_id фото
                duration_days=14
            )
            
            if request_id:
                # Отправляем уведомление админам с фото
                await notify_admins_about_new_adverts_with_photo(bot, adverts_data, user, request_id, photo_id)
                
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
            "❌ Пожалуйста, добавьте описание объявления к фото используя шаблон."
        )
        return 
    
    await state.clear()

async def notify_admins_about_new_adverts(bot: Bot, adverts_data: str, user: types.User, request_id: int):
    """Уведомляет админов о новом мероприятии (текст)"""
    try:
        
        admin_text = (
            "🎉 <b>НОВОЕ ОБЪЯВЛЕНИЕ НА МОДЕРАЦИЮ</b>\n\n"
            f"👤 <b>От:</b> {user.full_name}\n"
            f"📱 <b>Username:</b> @{user.username if user.username else 'нет'}\n"
            f"🆔 <b>User ID:</b> {user.id}\n"
            f"📋 <b>ID заявки:</b> #{request_id}\n"
            f"📅 <b>Длительность:</b> 14 дней\n\n"
            f"📝 <b>Описание объявления:</b>\n<code>{adverts_data}</code>\n\n"
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
        logging.error(f"Ошибка в notify_admins_about_new_adverts: {e}")

async def notify_admins_about_new_adverts_with_photo(bot: Bot, adverts_data: str, user: types.User, request_id: int, photo_id: str):
    """Уведомляет админов о новом мероприятии (фото + текст)"""
    try:
        
        caption = (
            "🎉 <b>НОВОЕ ОБЪЯВЛЕНИЕ НА МОДЕРАЦИЮ</b>\n\n"
            f"👤 <b>От:</b> {user.full_name}\n"
            f"📱 <b>Username:</b> @{user.username if user.username else 'нет'}\n"
            f"🆔 <b>User ID:</b> {user.id}\n"
            f"📋 <b>ID заявки:</b> #{request_id}\n"
            f"📅 <b>Длительность:</b> 14 дней\n\n"
            f"📝 <b>Описание объявления:</b>\n<code>{adverts_data}</code>\n\n"
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
        logging.error(f"Ошибка в notify_admins_about_new_adverts_with_photo: {e}")