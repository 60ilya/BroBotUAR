import logging
from aiogram import Router, types, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from config import Config
from db import Database
from keyboards.inline import transport_menu_ikb, transport_catalog_ikb, transport_partners_ikb, transport_agregator_ikb, back_start_menu, transport_request_ikb

router = Router()
db = Database()

class TransportStates(StatesGroup):
    waiting_for_transport_data = State() 

@router.callback_query(F.data == 'transport')
async def transport_menu(callback: types.CallbackQuery):
    
    text = """
🚗 Ищите машину в Кейптауне?
У меня собрана база проверенных партнёров с понятными условиями и скидками для подписчиков Бро Бота

💡 Бронируя через меня, Вы получаете скидку на итоговую сумму аренды:
<b>• 3% скидка</b> (при аренде до 15 дней)
<b>• 5% скидка</b> (при аренде от 15 дней до 1 месяца)
<b>• 6% скидка</b> на долгосрочную аренду (от 2 месяцев)
<b>• 5% скидка</b> при повторной аренде от меня (минимум 3 дня)

Всё просто: выбери партнёра, машину и оформи бронь 👇

<i>*Скидка суммируется со скидкой партнера</i>"""

    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_photo(
            photo=FSInputFile('app/content/menu_transport.jpg'),
            caption=text,
            reply_markup=transport_menu_ikb(),
            parse_mode="HTML"
        )
    
    
@router.callback_query(F.data == 'transport_catalog')
async def transport_catalog(callback: types.CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    
    text = """
<b>Перед тем как арендовать рекомендую ознакомиться с условиями рынка автомобилей тут есть два варианта аренды:</b>

1️⃣ Через сайт-агрегатор
Можно арендовать авто на крупных международных площадках — например, <i>Europcar, Woodford, Tempest, Pace Car Hire</i> и других.

💰 Цены начинаются примерно от R250 в сутки, и действительно часто ниже, чем у локальных прокатчиков.

💳 Оплата — только иностранной картой, условия бронирования и страховки указаны на самом сайте, есть компании, где дебетовая карта отлично прокатывает за кредитную, но нужно искать
 
⚠️ Имей в виду:
• возможны <b>задержки</b> с возвратом депозита (иногда до нескольких недель);
• некоторые компании работают только <b>по предоплате</b>;
• и не все принимают наличные (исключение — <i>Woodford, Tempest, Pace Car Hire</i>, они работают и с кэшем).

Если важно арендовать без карты или с локальной оплатой — смотрите вариант №2: аренда через местных партнёров.

2️⃣ <b>Через местных партнёров</b> 
За прошлый год, @adelsuprun собрала небольшую базу надежных партнеров те кто возвращают депозиты и следят за состоянием автомобилей, предоставляя сервис на протяжении всей аренды

<i>💡 Преимущества аренды через Бро Бота:</i>
• скидки до 5% в зависимости от срока аренды
• возможность общения с русскоязычными владельцами
• помощь в подборе автомобиля под даты и бюджет
• гибкие условия — без лишних комиссий

Чем раньше бронируете, тем больше выбор!"""

    
    await callback.message.answer(
        text,
        reply_markup=transport_catalog_ikb(),
        parse_mode="HTML"
    )

@router.callback_query(F.data == 'transport_agregator')
async def transport_agregator(callback: types.CallbackQuery):
    
    text = """
<b>Бронирование автомобилей через агрегатор</b>
нужна иностранная кредитная карта, самостоятельное бронирование

Бронируя по этим реф. ссылкам, вы вносите вклад в работу <b>Bro Bota</b>"""

    
    await callback.message.edit_text(
        text,
        reply_markup=transport_agregator_ikb(),
        parse_mode="HTML"
    )

@router.callback_query(F.data == 'transport_partners')
async def transport_agregator(callback: types.CallbackQuery):
    
    text = """
Выбирайте подходящие для вас условия и бронируйте автомобиль

<b>Партнер 1 - Вячеслав - сдача от 3х суток
Условия аренды:</b>
- От 200км/сутки
- Полная страховка на автомобиль (кроме шин) 
- От 7 дней доставка бесплатная 
- Депозит возвращается чаще всего сразу с оговоркой до 5 дней 
- Оплата принимается: RUB (перевод), USD, EUR, USDT любым удобным для вас методом
- Предоплата <b>10%</b> от суммы аренды (остаток суммы вносится после осмотра автомобиля и подписания договора аренды)

<i>*В случае аварии депозит не возвращается, все что свыше покрывает страховая компания</i>

При ДТП сразу необходимо звонить Вячеславу 


<b>Партнер 2 - Пауль Кабриолеты (скидка не работает бронь только через @adelsuprun) - сдача от 3х суток
Условия аренды: </b>
- От 150км сутки 
- От 7 дней доставка бесплатная 
- Полная страховка на автомобиль (кроме шин)
- Депозит возвращают сразу после сдачи авто
- Оплата принимается: USD, EUR, ZAR (оплатить можно картой или наличными)
- Предоплата <b>10%</b> от суммы аренды (остаток суммы вносится после осмотра автомобиля и подписания договора аренды)
(оплатить можно RUB или ZAR)

При ДТП сразу необходимо звонить Паулю


<b>Партнер 3 - Сергей - аренда в 5 городах Африки
Условия аренды:</b>
- от 150 км 
- Расширенная страховка приобретается отдельно (R100 - R200/сутки)
- Депозит возвращают от 5-10 дней 
- Оплата принимается: RUB, ZAR
- Предоплата 5000 RUB (остаток суммы вносится после осмотра автомобиля и подписания договора аренды)
- Предоставят автомобиль того же класса, в случаях непредвиденных обстоятельств

<b>Дополнительно оплачивается: </b>
- Мойка автомобиля R200 - R250 
- Второй водитель R50/день 

<b>Более точную информацию предоставит партнер перед бронированием</b>"""

    
    await callback.message.edit_text(
        text,
        reply_markup=transport_partners_ikb(),
        parse_mode="HTML"
    )

@router.callback_query(F.data.startswith('transport_partner_'))
async def transport_partner_request(callback: types.CallbackQuery):
    
    partner_number = int(callback.data.split('_')[-1])
    
    if partner_number == 1:
        partner = "Вячеславом"
        file_path = "app/content/Каталог_Вячеслав.pdf"
        url = "t.me/slavailjin"
    elif partner_number == 2:
        partner = "Паулем (связь через Адель)"
        file_path = "app/content/Каталог_Пауль.pdf"
        url = "t.me/adelsuprun"
    else:
        partner = "Сергеем (менеджер Екатерина)"
        file_path = "app/content/Каталог_Сергей.pdf"
        url = "t.me/lovkaya_77"
    
    text = f"""
Свяжитесь с партнером {partner}, также не забудьте указать важные данные для заявки:
1. Дата аренды
2. Количество человек
3. Пожелания по автомобилю
"""

    document = FSInputFile(file_path)
    
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(
            caption=text,
            document=document,
            reply_markup=transport_request_ikb(url),
            parse_mode="HTML"
        )

# # Обработчик текстового сообщения с данными заявки
# @router.message(TransportStates.waiting_for_transport_data, F.text)
# async def process_transport_data(message: types.Message, state: FSMContext, bot: Bot):
#     transport_data = message.text
#     user = message.from_user
    
#     # Добавляем/обновляем пользователя в БД
#     db.add_user(
#         tg_id=user.id,
#         username=user.username,
#         full_name=user.full_name
#     )
    
#     # Получаем пользователя из БД для получения ID
#     user_db = db.get_user(user.id)
    
#     if user_db:
#         # Сохраняем заявку в БД с выбранной длительностью
#         request_id = db.add_request(
#             user_id=user_db['id'],
#             request_type='transport',
#             text=transport_data,
#             duration_days=0
#         )
        
#         if request_id:
#             # Отправляем уведомление админам
#             await notify_admins_about_new_transport(bot, transport_data, user, request_id)
            
#             # Уведомляем пользователя
#             await message.answer(
#                 f"✅ Спасибо! Ваша заявка получена и отправлено на модерацию.\n",
#                 reply_markup=back_start_menu()
#             )
#         else:
#             await message.answer(
#                 "❌ Произошла ошибка при сохранении заявки. Попробуйте позже.",
#                 reply_markup=back_start_menu()
#             )
#     else:
#         await message.answer(
#             "❌ Ошибка при обработке вашего запроса. Попробуйте позже.",
#             reply_markup=back_start_menu()
#         )
    
#     # Сбрасываем состояние
#     await state.clear()
    
# async def notify_admins_about_new_transport(bot: Bot, transport_data: str, user: types.User, request_id: int):
#     """Уведомляет партнеров о новой заявке"""
#     try:
        
#         admin_text = (
#             "🎉 <b>НОВАЯ ЗАЯВКА ОТ БОТА</b>\n\n"
#             f"👤 <b>От:</b> {user.full_name}\n"
#             f"📱 <b>Username:</b> @{user.username if user.username else 'нет'}\n"
#             f"🆔 <b>User ID:</b> {user.id}\n"
#             f"📋 <b>ID заявки:</b> #{request_id}\n"
#             f"📝 <b>Описание заявки:</b>\n{transport_data}\n\n"
#         )
        
#         # Отправляем всем админам
#         for admin_id in Config.ADMIN_IDS:
#             try:
#                 await bot.send_message(
#                     chat_id=admin_id,
#                     text=admin_text,
#                     parse_mode="HTML"
#                 )
#             except Exception as e:
#                 logging.error(f"Ошибка отправки партнеру {admin_id}: {e}")
                
#     except Exception as e:
#         logging.error(f"Ошибка в notify_admins_about_new_transport: {e}")