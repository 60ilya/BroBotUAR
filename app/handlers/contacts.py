import logging
from aiogram import Router, types, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import Config
from db import Database
from keyboards.inline import contacts_menu_ikb, contacts_exchange_ikb, contacts_card_ikb

router = Router()
db = Database()

@router.callback_query(F.data == 'contacts')
async def contacts_menu(callback: types.CallbackQuery):
    text = """📄 Полезные контакты и поддержка"""
    
    try:
        await callback.message.edit_text(
            text,
            reply_markup=contacts_menu_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.delete()
        await callback.message.answer(
            text,
            reply_markup=contacts_menu_ikb(),
            parse_mode="HTML")
    
  
@router.callback_query(F.data == 'contacts_exchange')
async def contacts_exchange(callback: types.CallbackQuery):
    
    text = f"""
<b>💱 Обменный сервис, условия обмена:</b>

<b>Обмен валют:</b> USD, RUB, ZAR, EUR, NAD и другие 
<b>Обмен криптовалют:</b> USDT, BTC, ETH и другие

📍 Кейптаун и Йоханнесбург

<b>Преимущества:</b>
- Офис в центре города или доставим к вам
- Сопровождение сделок по покупке недвижимости 
- Оплата: счетов, услуг, авиабилетов, отелей, аренда и покупка машин, онлайн покупки, Airbnb
- Денежные переводы, выдача и принятие наличных <b>по всему миру</b>
<i>*Скидка при переводах от 10 000$</i>

Всегда <b>выгодные курсы</b> и отличный сервис
Узнать курс у менеджера <b>@conexuscrypto_manager</b>
Офис: <b>Google Maps</b> 📍
Режим работы 9:00 - 18:00

<b>👾 Отзывы - @conexus_crypto_reviews</b>"""

    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_video(
            video=types.FSInputFile('app/content/contacts_exchange.mp4'),
            caption=text,
            reply_markup=contacts_exchange_ikb(),
            parse_mode="HTML")
    
@router.callback_query(F.data == 'contacts_visa')
async def contacts_visa(callback: types.CallbackQuery):
    
    text = f"""
🇿🇦 Визы и Юридические услуги | <b>Планируете жить в Кейптауне на постоянной основе?

Нужна виза срочно? </b>
<i>используйте наш VIP-сервис — даем гарантию на получение визы в течение 3 месяцев</i>

⚡️ Туристические, партнёрские, студенческие, рабочие и бизнес-визы 
⚡️ Сопровождение от консультации до получения визы 
⚡️ Переводы, апостили, письма, стратегия подачи  

📍 <b>Офис в Кейптауне</b> | 37 Buitenkant St, 7925
🚩 <b>Telegram:</b> +27772632159 @yulia_concierge_attorney 
🌐 Наш сайт (https://concierge-attorneys.co.za/)

Спокойно. Надежно. Профессионально."""

    
    await callback.message.delete()
    await callback.message.answer_video(
        caption=text,
        video=types.FSInputFile('app/content/contacts_visa.mp4'),
        reply_markup=contacts_exchange_ikb(),
        parse_mode="HTML")

@router.callback_query(F.data == 'contacts_lie')
async def contacts_lie(callback: types.CallbackQuery):
    
    text = f"""Опишите подробно свою ситуацию сообщением @adelsuprun
По возможности приложите скрины, сообщения или записи разговоров."""

    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=contacts_exchange_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.delete()
        await callback.message.answer(
            text=text,
            reply_markup=contacts_exchange_ikb(),
            parse_mode="HTML")
    
@router.callback_query(F.data == 'contacts_card')
async def contacts_card(callback: types.CallbackQuery):
    
    text = f"""
<b>Международная карта для путешествий</b>

- Пластиковая 
- Оформление без доверенности 
- Оформляется за 2 дня 
- Обслуживание — бесплатно 
- Именная или нет — на выбор 
- Привязывается к РФ номеру 
- Пополнение рублями через СБП 

*Доставка по всему миру промокод "<b>КЕЙПТАУН</b>" скидка 1 000RUB

Путешествуйте с комфортом, <b>КРЯ</b>

<b>Отзывы</b> @oplataguruproofs"""

    # Все фото группой (только к первому текст)
    media = [
        types.InputMediaPhoto(
            media=types.FSInputFile(f"app/content/contacts_{i}.jpg")
        ) for i in range(1, 4)
    ]
    await callback.message.answer_media_group(media=media)
    
    # Клавиатура отдельным сообщением
    await callback.message.answer(
        text,
        reply_markup=contacts_card_ikb(),
        parse_mode="HTML"
    )