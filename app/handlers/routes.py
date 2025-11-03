import logging
from aiogram import Router, types, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import Config
from db import Database
from keyboards.inline import *

router = Router()
db = Database()


@router.callback_query(F.data == 'routes')
async def routes(callback: types.CallbackQuery):
    
    text = """
Ваш BroBOT помощник здесь 🌴
Хочу помочь спланировать незабываемое путешествие по Кейптауну 😉

Сначала мне надо задать несколько вопросов"""

    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_menu(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_menu(),
            parse_mode="HTML")
    
@router.callback_query(F.data == 'routes_start')
async def routes_start(callback: types.CallbackQuery):
    
    text = """
С кем путешествуете?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_start_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_start_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two')
@router.callback_query(F.data == 'routes_alone')
@router.callback_query(F.data == 'routes_family')
@router.callback_query(F.data == 'routes_friends')
async def routes_two(callback: types.CallbackQuery):
    
    text = """
На чем собираетесь передвигаться?"""
    
    data = callback.data.split('_')[-1]
    
    match data:
        case "two":
            text = "На чем собираетесь передвигаться?"
            reply_markup=routes_two_ikb()
        case "alone":
            text = "На чем собираетесь передвигаться?"
            reply_markup=routes_alone_ikb()
        case "family":
            text = "Что Вас больше всего интересует?"
            reply_markup=routes_family_ikb()
        case "friends":
            text = "На чем собираетесь передвигаться?"
            reply_markup=routes_friends_ikb()
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=reply_markup,
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text=text,
            reply_markup=reply_markup,
            parse_mode="HTML")

        
@router.callback_query(F.data == 'routes_two_tran')
async def routes_transport_transfer(callback: types.CallbackQuery):
    
    text = """
<b>💡 Совет от Бро Бота: </b>
Помните, если хотите комфорт и безопасность, выбирайте такси через агрегатор (Bolt, Uber) или  <b><u>красный автобус</u></b>
    
<i>*Помните общественный транспорт для местных</i>
    
Что вас больше всего интересует?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_int_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_int_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_nat')
async def routes_two_nat(callback: types.CallbackQuery):
    
    text = """
Из природных мест в Кейптауне есть парки, горы, водопады

В путеводителе по Кейптауну  несколько страниц посвящено природным местам

<b>Выберите, что интересно:</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_nat_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_nat_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_food')
async def routes_two_food(callback: types.CallbackQuery):
    
    text = """
Что Вам подсказать?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_food_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_food_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_break')
async def routes_two_break(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_break_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_break_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_lun')
async def routes_two_lun(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_lun_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_lun_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_din')
async def routes_two_din(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_din_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_din_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_cof')
async def routes_two_cof(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_cof_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_cof_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_ani')
async def routes_two_ani(callback: types.CallbackQuery):
    
    text = """
В Кейптауне животных можно встретить почти на каждом шагу 🐾
    
🦁 В районе Кейптауна — два сафари-парка:
один прямо в черте Кейпа, второй за его пределами, где можно увидеть «большую пятёрку» — львов, слонов, буйволов, носорогов и леопардов
🐧 На пляже <b>Boulders Beach</b> живёт колония африканских пингвинов — они спокойно гуляют по песку и купаются рядом с людьми
На побережье встречаются морские котики, пеликаны и пингвины, а в лагунах и болотах — целые стаи фламинго.
🦙 В городе и за его пределами есть фермы с альпаками, козами, страусами и жирафами — можно покормить, погладить и сделать фото с видом на горы
🐦 Для наблюдения за птицами стоит заглянуть в <b>Rondevlei Nature Reserve</b> — десятки видов водоплавающих и красивые маршруты по настилам
🦈 Хочется больше адреналина? Попробуйте снорклинг с тюленями в Hout Bay или сафари-поездку в <b>Aquila Reserve</b> — эмоций хватит надолго

Больше локаций, фото и маршрутов — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_ani_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_ani_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_cult')
async def routes_two_cult(callback: types.CallbackQuery):
    
    text = """
Кейптаун настоящая культурная столица Южной Африки

🎨 Здесь живёт огромное комьюнити художников, музыкантов и дизайнеров. Город пропитан творчеством  от уличных муралов в Woodstock до галерей в центре

⛪️ Можно прогуляться по старинным церквям и музеям, заглянуть в арт-пространства и вечерние джаз-бары, где играют живую музыку

🕯 А по четвергам загляните на <b>First Thursdays</b> — когда весь центр превращается в одну большую выставку: галереи, музыка, уличная еда и бокал вина в руке

Основной район <b>City Bowl</b> улицы Bree Street, Kloof Street, Loop Street, Long Street

Больше галерей, маршрутов и атмосферных мест — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_cult_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_cult_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_ext')
async def routes_two_ext(callback: types.CallbackQuery):
    
    text = """
В Кейптауне можно заняться любыми активностями от серфинга и параглайдинга до дайвинга с акулами

Здесь есть зиплайны, квадроциклы, оффроад-багги, мотокросс, банджи-джампинг, стрельбища, вейкбординг, каякинг, хайкинг, абсейл со Столовой горы и даже ледяные купания в океане с баней 

Важно Кейптаун это место, где все лучше бронировать заранее, тем более когда вы едете в сезон"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_ext_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_ext_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_shop')
async def routes_two_shop(callback: types.CallbackQuery):
    
    text = """
Рай для шопоголиков, коллекционеров редкостей и ценителей ручной работы

Здесь рождаются локальные бренды с душой: одежда из натуральных тканей, украшения ручной работы, предметы интерьера и ароматы, созданные художниками, а не фабриками

🎨 Местные творческие, яркие и открытые люди, и это чувствуется во всём, что они делают: качество, идея и характер в каждой детали

🛒 За атмосферой в <b>The Old Biscuit Mill</b> (Woodstock) или <b>Mojo Market</b> (Sea Point).
За шопингом <b>V&A Waterfront</b>, <b>Canal Walk</b>, <b>Cavendish Square</b>

🧵 А если хочешь уникальное загляните в путеводитель"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_shop_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_shop_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_bars')
async def routes_two_bars(callback: types.CallbackQuery):
    
    text = """
Кейптаун славится своими атмосферными барами и вечеринками у океана

Здесь можно провести вечер в джаз-баре на Bree Street,пить коктейли на крыше с видом на закат в Camps Bayили танцевать под афробит до рассвета на Long Street

Любителям вина стоит заглянуть в Constantia или на винные бары в центре, а тем, кто ищет камерную атмосферу в тайные спикизи или андеграунд-клубы на Kloof Street

Более подробную подборку лучших баров, мест с живой музыкой, крафтовым пивом и заведений 18+ можно найти в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_bars_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_bars_ikb(),
            parse_mode="HTML")

        
@router.callback_query(F.data == 'routes_two_him')
async def routes_transport_himself(callback: types.CallbackQuery):
    
    text = """
Что вас больше всего интересует?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_int_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_int_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_him_nat')
async def routes_two_him_nat(callback: types.CallbackQuery):
    
    text = """
Путешествовать по Кейптауну вдвоём значит иметь собственную маленькую свободу

На машине можно за день увидеть всё от виноградников до пляжей с пингвинами

🚙 Поезжайте в сторону <b>Chapman’s Peak Drive</b> - это одна из самых красивых прибрежных дорог в мире
Сделайте остановку в <b>Noordhoek</b>, пообедайте в <b>Cape Point Vineyards</b>,а потом спуститесь к <b>Boulders Beach</b>, где живут африканские пингвины
🌄 Если хочется природы отправляйтесь в <b>Cape Point National Park</b> или выше в горы <b>Silvermine</b>.
Там отличные маршруты для хайкинга, пикников и фото с панорамами
🍷 А если день обещает быть ленивым винные фермы <b>Constantia</b> и <b>Stellenbosch</b> ждут: дегустации, рестораны и уют вдвоём

📘 В Путеводителе по Кейптауне есть три готовых маршрута на весь день """
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_nat_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_nat_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_him_food')
async def routes_two_him_food(callback: types.CallbackQuery):
    
    text = """
Что Вам подсказать?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_food_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_food_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_him_break')
async def routes_two_him_break(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_break_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_break_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_him_lun')
async def routes_two_him_lun(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_lun_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_lun_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_him_din')
async def routes_two_him_din(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_din_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_din_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_two_him_cof')
async def routes_two_him_cof(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_cof_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_cof_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_him_ani')
async def routes_two_him_ani(callback: types.CallbackQuery):
    
    text = """
В Кейптауне животных можно встретить почти на каждом шагу 🐾

🦁 В районе Кейптауна — два сафари-парка:один прямо в черте Кейпа, второй за его пределами, где можно увидеть «большую пятёрку» — львов, слонов, буйволов, носорогов и леопардов

🐧 На пляже <b>Boulders Beach</b> живёт колония африканских пингвинов — они спокойно гуляют по песку и купаются рядом с людьмиНа побережье встречаются морские котики, пеликаны и пингвины, а в лагунах и болотах — целые стаи фламинго.ё
🦙 В городе и за его пределами есть фермы с альпаками, козами, страусами и жирафами — можно покормить, погладить и сделать фото с видом на горы
🐦 Для наблюдения за птицами стоит заглянуть в <b>Rondevlei Nature Reserve</b> — десятки видов водоплавающих и красивые маршруты по настилам
🦈 Хочется больше адреналина? Попробуйте снорклинг с тюленями в Hout Bay или сафари-поездку в <b>Aquila Reserve</b> — эмоций хватит надолго

Больше локаций, фото и маршрутов — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_ani_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_ani_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_him_cult')
async def routes_two_him_cult(callback: types.CallbackQuery):
    
    text = """
Кейптаун настоящая культурная столица Южной Африки

🎨 Здесь живёт огромное комьюнити художников, музыкантов и дизайнеров. Город пропитан творчеством  от уличных муралов в Woodstock до галерей в центре

⛪️ Можно прогуляться по старинным церквям и музеям, заглянуть в арт-пространства и вечерние джаз-бары, где играют живую музыку

🕯 А по четвергам загляните на <b>First Thursdays</b> — когда весь центр превращается в одну большую выставку: галереи, музыка, уличная еда и бокал вина в руке

Основной район <b>City Bowl</b> улицы Bree Street, Kloof Street, Loop Street, Long Street

Больше галерей, маршрутов и атмосферных мест — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_cult_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_cult_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_him_ext')
async def routes_two_him_ext(callback: types.CallbackQuery):
    
    text = """
В Кейптауне можно заняться любыми активностями от серфинга и параглайдинга до дайвинга с акулами

Здесь есть зиплайны, квадроциклы, оффроад-багги, мотокросс, банджи-джампинг, стрельбища, вейкбординг, каякинг, хайкинг, абсейл со Столовой горы и даже ледяные купания в океане с баней 

<b>Важно</b> Кейптаун это место, где все лучше бронировать заранее, тем более когда вы едете в сезон"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_ext_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_ext_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_him_shop')
async def routes_two_him_shop(callback: types.CallbackQuery):
    
    text = """
Рай для шопоголиков, коллекционеров редкостей и ценителей ручной работы

Здесь рождаются локальные бренды с душой: одежда из натуральных тканей, украшения ручной работы, предметы интерьера и ароматы, созданные художниками, а не фабриками

🎨 Местные творческие, яркие и открытые люди, и это чувствуется во всём, что они делают: качество, идея и характер в каждой детали

🛒 За атмосферой в <b>The Old Biscuit Mill</b> (Woodstock) или <b>Mojo Market</b> (Sea Point).
За шопингом <b>V&A Waterfront</b>, <b>Canal Walk</b>, <b>Cavendish Square</b>

🧵 А если хочешь уникальное загляните в путеводитель"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_shop_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_shop_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_two_him_bars')
async def routes_two_him_bars(callback: types.CallbackQuery):
    
    text = """
Кейптаун славится своими атмосферными барами и вечеринками у океана

Здесь можно провести вечер в джаз-баре на Bree Street,пить коктейли на крыше с видом на закат в Camps Bayили танцевать под афробит до рассвета на Long Street

Любителям вина стоит заглянуть в Constantia или на винные бары в центре, а тем, кто ищет камерную атмосферу в тайные спикизи или андеграунд-клубы на Kloof Street

Более подробную подборку лучших баров, мест с живой музыкой, крафтовым пивом и заведений 18+ можно найти в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_two_him_bars_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_two_him_bars_ikb(),
            parse_mode="HTML")
        

@router.callback_query(F.data == 'routes_alone_tran')
async def routes_alone_tran(callback: types.CallbackQuery):
    
    text = """
<b>💡 Совет от Бро Бота: </b>
Помните, если хотите комфорт и безопасность, выбирайте такси через агрегатор (Bolt, Uber) или  <b><u>красный автобус</u></b>
    
<i>*Помните общественный транспорт для местных</i>
    
Что вас больше всего интересует?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_int_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_int_ikb(),
            parse_mode="HTML")
           
@router.callback_query(F.data == 'routes_alone_nat')
async def routes_alone_nat(callback: types.CallbackQuery):
    
    text = """
Из природных мест в Кейптауне есть парки, горы, водопады

В путеводителе по Кейптауну  несколько страниц посвящено природным местам

<b>Выберите, что интересно:</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_nat_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_nat_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_food')
async def routes_alone_food(callback: types.CallbackQuery):
    
    text = """
Что Вам подсказать?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_food_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_food_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_break')
async def routes_alone_break(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_break_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_break_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_lun')
async def routes_alone_lun(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_lun_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_lun_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_din')
async def routes_alone_din(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_din_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_din_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_cof')
async def routes_alone_cof(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_cof_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_cof_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_ani')
async def routes_alone_ani(callback: types.CallbackQuery):
    
    text = """
В Кейптауне животных можно встретить почти на каждом шагу 🐾
    
🦁 В районе Кейптауна — два сафари-парка:
один прямо в черте Кейпа, второй за его пределами, где можно увидеть «большую пятёрку» — львов, слонов, буйволов, носорогов и леопардов
🐧 На пляже <b>Boulders Beach</b> живёт колония африканских пингвинов — они спокойно гуляют по песку и купаются рядом с людьми
На побережье встречаются морские котики, пеликаны и пингвины, а в лагунах и болотах — целые стаи фламинго.
🦙 В городе и за его пределами есть фермы с альпаками, козами, страусами и жирафами — можно покормить, погладить и сделать фото с видом на горы
🐦 Для наблюдения за птицами стоит заглянуть в <b>Rondevlei Nature Reserve</b> — десятки видов водоплавающих и красивые маршруты по настилам
🦈 Хочется больше адреналина? Попробуйте снорклинг с тюленями в Hout Bay или сафари-поездку в <b>Aquila Reserve</b> — эмоций хватит надолго

Больше локаций, фото и маршрутов — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_ani_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_ani_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_cult')
async def routes_alone_cult(callback: types.CallbackQuery):
    
    text = """
Кейптаун настоящая культурная столица Южной Африки

🎨 Здесь живёт огромное комьюнити художников, музыкантов и дизайнеров. Город пропитан творчеством  от уличных муралов в Woodstock до галерей в центре

⛪️ Можно прогуляться по старинным церквям и музеям, заглянуть в арт-пространства и вечерние джаз-бары, где играют живую музыку

🕯 А по четвергам загляните на <b>First Thursdays</b> — когда весь центр превращается в одну большую выставку: галереи, музыка, уличная еда и бокал вина в руке

Основной район <b>City Bowl</b> улицы Bree Street, Kloof Street, Loop Street, Long Street

Больше галерей, маршрутов и атмосферных мест — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_cult_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_cult_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_ext')
async def routes_alone_ext(callback: types.CallbackQuery):
    
    text = """
В Кейптауне можно заняться любыми активностями от серфинга и параглайдинга до дайвинга с акулами

Здесь есть зиплайны, квадроциклы, оффроад-багги, мотокросс, банджи-джампинг, стрельбища, вейкбординг, каякинг, хайкинг, абсейл со Столовой горы и даже ледяные купания в океане с баней 

Важно Кейптаун это место, где все лучше бронировать заранее, тем более когда вы едете в сезон"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_ext_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_ext_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_shop')
async def routes_alone_shop(callback: types.CallbackQuery):
    
    text = """
Рай для шопоголиков, коллекционеров редкостей и ценителей ручной работы

Здесь рождаются локальные бренды с душой: одежда из натуральных тканей, украшения ручной работы, предметы интерьера и ароматы, созданные художниками, а не фабриками

🎨 Местные творческие, яркие и открытые люди, и это чувствуется во всём, что они делают: качество, идея и характер в каждой детали

🛒 За атмосферой в <b>The Old Biscuit Mill</b> (Woodstock) или <b>Mojo Market</b> (Sea Point).
За шопингом <b>V&A Waterfront</b>, <b>Canal Walk</b>, <b>Cavendish Square</b>

🧵 А если хочешь уникальное загляните в путеводитель"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_shop_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_shop_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_bars')
async def routes_alone_bars(callback: types.CallbackQuery):
    
    text = """
Кейптаун славится своими атмосферными барами и вечеринками у океана

Здесь можно провести вечер в джаз-баре на Bree Street,пить коктейли на крыше с видом на закат в Camps Bayили танцевать под афробит до рассвета на Long Street

Любителям вина стоит заглянуть в Constantia или на винные бары в центре, а тем, кто ищет камерную атмосферу в тайные спикизи или андеграунд-клубы на Kloof Street

Более подробную подборку лучших баров, мест с живой музыкой, крафтовым пивом и заведений 18+ можно найти в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_bars_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_bars_ikb(),
            parse_mode="HTML")


@router.callback_query(F.data == 'routes_alone_him')
async def routes_alone_him(callback: types.CallbackQuery):
    
    text = """
Что вас больше всего интересует?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_int_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_int_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_him_nat')
async def routes_alone_him_nat(callback: types.CallbackQuery):
    
    text = """
Из природных мест в Кейптауне есть парки, горы, водопады

В путеводителе по Кейптауну  несколько страниц посвящено природным местам

<b>Выберите, что интересно:</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_nat_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_nat_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_him_food')
async def routes_alone_him_food(callback: types.CallbackQuery):
    
    text = """
Что Вам подсказать?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_food_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_food_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_him_break')
async def routes_alone_him_break(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_break_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_break_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_him_lun')
async def routes_alone_him_lun(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_lun_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_lun_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_him_din')
async def routes_alone_him_din(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_din_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_din_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_alone_him_cof')
async def routes_alone_him_cof(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_cof_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_cof_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_him_ani')
async def routes_alone_him_ani(callback: types.CallbackQuery):
    
    text = """
В Кейптауне животных можно встретить почти на каждом шагу 🐾

🦁 В районе Кейптауна — два сафари-парка:один прямо в черте Кейпа, второй за его пределами, где можно увидеть «большую пятёрку» — львов, слонов, буйволов, носорогов и леопардов

🐧 На пляже <b>Boulders Beach</b> живёт колония африканских пингвинов — они спокойно гуляют по песку и купаются рядом с людьмиНа побережье встречаются морские котики, пеликаны и пингвины, а в лагунах и болотах — целые стаи фламинго.ё
🦙 В городе и за его пределами есть фермы с альпаками, козами, страусами и жирафами — можно покормить, погладить и сделать фото с видом на горы
🐦 Для наблюдения за птицами стоит заглянуть в <b>Rondevlei Nature Reserve</b> — десятки видов водоплавающих и красивые маршруты по настилам
🦈 Хочется больше адреналина? Попробуйте снорклинг с тюленями в Hout Bay или сафари-поездку в <b>Aquila Reserve</b> — эмоций хватит надолго

Больше локаций, фото и маршрутов — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_ani_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_ani_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_him_cult')
async def routes_alone_him_cult(callback: types.CallbackQuery):
    
    text = """
Кейптаун настоящая культурная столица Южной Африки

🎨 Здесь живёт огромное комьюнити художников, музыкантов и дизайнеров. Город пропитан творчеством  от уличных муралов в Woodstock до галерей в центре

⛪️ Можно прогуляться по старинным церквям и музеям, заглянуть в арт-пространства и вечерние джаз-бары, где играют живую музыку

🕯 А по четвергам загляните на <b>First Thursdays</b> — когда весь центр превращается в одну большую выставку: галереи, музыка, уличная еда и бокал вина в руке

Основной район <b>City Bowl</b> улицы Bree Street, Kloof Street, Loop Street, Long Street

Больше галерей, маршрутов и атмосферных мест — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_cult_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_cult_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_him_ext')
async def routes_alone_him_ext(callback: types.CallbackQuery):
    
    text = """
В Кейптауне можно заняться любыми активностями от серфинга и параглайдинга до дайвинга с акулами

Здесь есть зиплайны, квадроциклы, оффроад-багги, мотокросс, банджи-джампинг, стрельбища, вейкбординг, каякинг, хайкинг, абсейл со Столовой горы и даже ледяные купания в океане с баней 

<b>Важно</b> Кейптаун это место, где все лучше бронировать заранее, тем более когда вы едете в сезон"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_ext_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_ext_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_him_shop')
async def routes_alone_him_shop(callback: types.CallbackQuery):
    
    text = """
Рай для шопоголиков, коллекционеров редкостей и ценителей ручной работы

Здесь рождаются локальные бренды с душой: одежда из натуральных тканей, украшения ручной работы, предметы интерьера и ароматы, созданные художниками, а не фабриками

🎨 Местные творческие, яркие и открытые люди, и это чувствуется во всём, что они делают: качество, идея и характер в каждой детали

🛒 За атмосферой в <b>The Old Biscuit Mill</b> (Woodstock) или <b>Mojo Market</b> (Sea Point).
За шопингом <b>V&A Waterfront</b>, <b>Canal Walk</b>, <b>Cavendish Square</b>

🧵 А если хочешь уникальное загляните в путеводитель"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_shop_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_shop_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_alone_him_bars')
async def routes_alone_him_bars(callback: types.CallbackQuery):
    
    text = """
Кейптаун славится своими атмосферными барами и вечеринками у океана

Здесь можно провести вечер в джаз-баре на Bree Street,пить коктейли на крыше с видом на закат в Camps Bayили танцевать под афробит до рассвета на Long Street

Любителям вина стоит заглянуть в Constantia или на винные бары в центре, а тем, кто ищет камерную атмосферу в тайные спикизи или андеграунд-клубы на Kloof Street

Более подробную подборку лучших баров, мест с живой музыкой, крафтовым пивом и заведений 18+ можно найти в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_alone_him_bars_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_alone_him_bars_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fam_nat')
async def routes_fam_nat(callback: types.CallbackQuery):
    
    text = """
Из природных мест в Кейптауне есть парки, горы, водопады, хайки

В путеводителе по Кейптауну  несколько страниц посвящено природным местам

<b>Выберите, что интересно:</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_nat_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_nat_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fam_food')
async def routes_fam_food(callback: types.CallbackQuery):
    
    text = """
Что Вам подсказать?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_food_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_food_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fam_break')
async def routes_fam_break(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_break_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_break_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fam_lun')
async def routes_fam_lun(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_lun_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_lun_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fam_din')
async def routes_fam_din(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_din_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_din_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fam_cof')
async def routes_fam_cof(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_cof_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_cof_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fam_ani')
async def routes_fam_ani(callback: types.CallbackQuery):
    
    text = """
В Кейптауне животных можно встретить почти на каждом шагу 🐾
    
🦁 В районе Кейптауна — два сафари-парка:
один прямо в черте Кейпа, второй за его пределами, где можно увидеть «большую пятёрку» — львов, слонов, буйволов, носорогов и леопардов
🐧 На пляже <b>Boulders Beach</b> живёт колония африканских пингвинов — они спокойно гуляют по песку и купаются рядом с людьми
На побережье встречаются морские котики, пеликаны и пингвины, а в лагунах и болотах — целые стаи фламинго.
🦙 В городе и за его пределами есть фермы с альпаками, козами, страусами и жирафами — можно покормить, погладить и сделать фото с видом на горы
🐦 Для наблюдения за птицами стоит заглянуть в <b>Rondevlei Nature Reserve</b> — десятки видов водоплавающих и красивые маршруты по настилам
🦈 Хочется больше адреналина? Попробуйте снорклинг с тюленями в Hout Bay или сафари-поездку в <b>Aquila Reserve</b> — эмоций хватит надолго

Больше локаций, фото и маршрутов — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_ani_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_ani_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fam_cult')
async def routes_fam_cult(callback: types.CallbackQuery):
    
    text = """
Кейптаун настоящая культурная столица Южной Африки

🎨 Здесь живёт огромное комьюнити художников, музыкантов и дизайнеров. Город пропитан творчеством  от уличных муралов в Woodstock до галерей в центре

⛪️ Можно прогуляться по старинным церквям и музеям, заглянуть в арт-пространства и вечерние джаз-бары, где играют живую музыку

🕯 А по четвергам загляните на <b>First Thursdays</b> — когда весь центр превращается в одну большую выставку: галереи, музыка, уличная еда и бокал вина в руке

Основной район <b>City Bowl</b> улицы Bree Street, Kloof Street, Loop Street, Long Street

Больше галерей, маршрутов и атмосферных мест — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_cult_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_cult_ikb(),
            parse_mode="HTML")       
        
@router.callback_query(F.data == 'routes_fam_shop')
async def routes_fam_shop(callback: types.CallbackQuery):
    
    text = """
Рай для шопоголиков, коллекционеров редкостей и ценителей ручной работы

Здесь рождаются локальные бренды с душой: одежда из натуральных тканей, украшения ручной работы, предметы интерьера и ароматы, созданные художниками, а не фабриками

🎨 Местные творческие, яркие и открытые люди, и это чувствуется во всём, что они делают: качество, идея и характер в каждой детали

🛒 За атмосферой в <b>The Old Biscuit Mill</b> (Woodstock) или <b>Mojo Market</b> (Sea Point).
За шопингом <b>V&A Waterfront</b>, <b>Canal Walk</b>, <b>Cavendish Square</b>

🧵 А если хочешь уникальное загляните в путеводитель"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fam_shop_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fam_shop_ikb(),
            parse_mode="HTML")


@router.callback_query(F.data == 'routes_fri_tran')
async def routes_fri_tran(callback: types.CallbackQuery):
    
    text = """
<b>💡 Совет от Бро Бота: </b>
Помните, если хотите комфорт и безопасность, выбирайте такси через агрегатор (Bolt, Uber) или  <b><u>красный автобус</u></b>
    
<i>*Помните общественный транспорт для местных</i>
    
Что вас больше всего интересует?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_int_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_int_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_nat')
async def routes_fri_nat(callback: types.CallbackQuery):
    
    text = """
Из природных мест в Кейптауне есть парки, горы, водопады, хайки

В путеводителе по Кейптауну  несколько страниц посвящено природным местам

<b>Выберите, что интересно:</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_nat_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_nat_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_food')
async def routes_fri_food(callback: types.CallbackQuery):
    
    text = """
Что Вам подсказать?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_food_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_food_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_break')
async def routes_fri_break(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_break_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_break_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_lun')
async def routes_fri_lun(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_lun_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_lun_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_din')
async def routes_fri_din(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_din_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_din_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_cof')
async def routes_fri_cof(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_cof_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_cof_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_ani')
async def routes_fri_ani(callback: types.CallbackQuery):
    
    text = """
В Кейптауне животных можно встретить почти на каждом шагу 🐾
    
🦁 В районе Кейптауна — два сафари-парка:
один прямо в черте Кейпа, второй за его пределами, где можно увидеть «большую пятёрку» — львов, слонов, буйволов, носорогов и леопардов
🐧 На пляже <b>Boulders Beach</b> живёт колония африканских пингвинов — они спокойно гуляют по песку и купаются рядом с людьми
На побережье встречаются морские котики, пеликаны и пингвины, а в лагунах и болотах — целые стаи фламинго.
🦙 В городе и за его пределами есть фермы с альпаками, козами, страусами и жирафами — можно покормить, погладить и сделать фото с видом на горы
🐦 Для наблюдения за птицами стоит заглянуть в <b>Rondevlei Nature Reserve</b> — десятки видов водоплавающих и красивые маршруты по настилам
🦈 Хочется больше адреналина? Попробуйте снорклинг с тюленями в Hout Bay или сафари-поездку в <b>Aquila Reserve</b> — эмоций хватит надолго

Больше локаций, фото и маршрутов — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_ani_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_ani_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_cult')
async def routes_fri_cult(callback: types.CallbackQuery):
    
    text = """
Кейптаун настоящая культурная столица Южной Африки

🎨 Здесь живёт огромное комьюнити художников, музыкантов и дизайнеров. Город пропитан творчеством  от уличных муралов в Woodstock до галерей в центре

⛪️ Можно прогуляться по старинным церквям и музеям, заглянуть в арт-пространства и вечерние джаз-бары, где играют живую музыку

🕯 А по четвергам загляните на <b>First Thursdays</b> — когда весь центр превращается в одну большую выставку: галереи, музыка, уличная еда и бокал вина в руке

Основной район <b>City Bowl</b> улицы Bree Street, Kloof Street, Loop Street, Long Street

Больше галерей, маршрутов и атмосферных мест — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_cult_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_cult_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_ext')
async def routes_fri_ext(callback: types.CallbackQuery):
    
    text = """
В Кейптауне можно заняться любыми активностями от серфинга и параглайдинга до дайвинга с акулами

Здесь есть зиплайны, квадроциклы, оффроад-багги, мотокросс, банджи-джампинг, стрельбища, вейкбординг, каякинг, хайкинг, абсейл со Столовой горы и даже ледяные купания в океане с баней 

Важно Кейптаун это место, где все лучше бронировать заранее, тем более когда вы едете в сезон"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_ext_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_ext_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_shop')
async def routes_fri_shop(callback: types.CallbackQuery):
    
    text = """
Рай для шопоголиков, коллекционеров редкостей и ценителей ручной работы

Здесь рождаются локальные бренды с душой: одежда из натуральных тканей, украшения ручной работы, предметы интерьера и ароматы, созданные художниками, а не фабриками

🎨 Местные творческие, яркие и открытые люди, и это чувствуется во всём, что они делают: качество, идея и характер в каждой детали

🛒 За атмосферой в <b>The Old Biscuit Mill</b> (Woodstock) или <b>Mojo Market</b> (Sea Point).
За шопингом <b>V&A Waterfront</b>, <b>Canal Walk</b>, <b>Cavendish Square</b>

🧵 А если хочешь уникальное загляните в путеводитель"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_shop_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_shop_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_bars')
async def routes_fri_bars(callback: types.CallbackQuery):
    
    text = """
💡 Совет от Бро Бота:
в Кейптауне культура это не экскурсия, а состояние
Главное — не пытайся всё успеть, просто идти туда, где сегодня играет музыка

Кейптаун славится своими атмосферными барами и вечеринками у океана

Здесь можно провести вечер в джаз-баре на Bree Street,пить коктейли на крыше с видом на закат в Camps Bayили танцевать под афробит до рассвета на Long Street

Любителям вина стоит заглянуть в Constantia или на винные бары в центре, а тем, кто ищет камерную атмосферу в тайные спикизи или андеграунд-клубы на Kloof Street

Более подробную подборку лучших баров, мест с живой музыкой, крафтовым пивом и заведений 18+ можно найти в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_bars_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_bars_ikb(),
            parse_mode="HTML")

        
@router.callback_query(F.data == 'routes_fri_him')
async def routes_fri_him(callback: types.CallbackQuery):
    
    text = """
Что вас больше всего интересует?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_int_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_int_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_him_nat')
async def routes_fri_him_nat(callback: types.CallbackQuery):
    
    text = """
Из природных мест в Кейптауне есть парки, горы, водопады, хайки

В путеводителе по Кейптауну  несколько страниц посвящено природным местам

<b>Выберите, что интересно:</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_nat_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_nat_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_him_food')
async def routes_fri_him_food(callback: types.CallbackQuery):
    
    text = """
Что Вам подсказать?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_food_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_food_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_him_break')
async def routes_fri_him_break(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_break_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_break_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_him_lun')
async def routes_fri_him_lun(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_lun_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_lun_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_him_din')
async def routes_fri_him_din(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_din_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_din_ikb(),
            parse_mode="HTML")
        
@router.callback_query(F.data == 'routes_fri_him_cof')
async def routes_fri_him_cof(callback: types.CallbackQuery):
    
    text = """
В каком районе остановились?"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_cof_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_cof_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_him_ani')
async def routes_fri_him_ani(callback: types.CallbackQuery):
    
    text = """
В Кейптауне животных можно встретить почти на каждом шагу 🐾

🦁 В районе Кейптауна — два сафари-парка:один прямо в черте Кейпа, второй за его пределами, где можно увидеть «большую пятёрку» — львов, слонов, буйволов, носорогов и леопардов

🐧 На пляже <b>Boulders Beach</b> живёт колония африканских пингвинов — они спокойно гуляют по песку и купаются рядом с людьмиНа побережье встречаются морские котики, пеликаны и пингвины, а в лагунах и болотах — целые стаи фламинго.ё
🦙 В городе и за его пределами есть фермы с альпаками, козами, страусами и жирафами — можно покормить, погладить и сделать фото с видом на горы
🐦 Для наблюдения за птицами стоит заглянуть в <b>Rondevlei Nature Reserve</b> — десятки видов водоплавающих и красивые маршруты по настилам
🦈 Хочется больше адреналина? Попробуйте снорклинг с тюленями в Hout Bay или сафари-поездку в <b>Aquila Reserve</b> — эмоций хватит надолго

Больше локаций, фото и маршрутов — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_ani_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_ani_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_him_cult')
async def routes_fri_him_cult(callback: types.CallbackQuery):
    
    text = """
Кейптаун настоящая культурная столица Южной Африки

🎨 Здесь живёт огромное комьюнити художников, музыкантов и дизайнеров. Город пропитан творчеством  от уличных муралов в Woodstock до галерей в центре

⛪️ Можно прогуляться по старинным церквям и музеям, заглянуть в арт-пространства и вечерние джаз-бары, где играют живую музыку

🕯 А по четвергам загляните на <b>First Thursdays</b> — когда весь центр превращается в одну большую выставку: галереи, музыка, уличная еда и бокал вина в руке

Основной район <b>City Bowl</b> улицы Bree Street, Kloof Street, Loop Street, Long Street

Больше галерей, маршрутов и атмосферных мест — в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_cult_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_cult_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_him_ext')
async def routes_fri_him_ext(callback: types.CallbackQuery):
    
    text = """
В Кейптауне можно заняться любыми активностями от серфинга и параглайдинга до дайвинга с акулами

Здесь есть зиплайны, квадроциклы, оффроад-багги, мотокросс, банджи-джампинг, стрельбища, вейкбординг, каякинг, хайкинг, абсейл со Столовой горы и даже ледяные купания в океане с баней 

<b>Важно</b> Кейптаун это место, где все лучше бронировать заранее, тем более когда вы едете в сезон"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_ext_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_ext_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_him_shop')
async def routes_fri_him_shop(callback: types.CallbackQuery):
    
    text = """
Рай для шопоголиков, коллекционеров редкостей и ценителей ручной работы

Здесь рождаются локальные бренды с душой: одежда из натуральных тканей, украшения ручной работы, предметы интерьера и ароматы, созданные художниками, а не фабриками

🎨 Местные творческие, яркие и открытые люди, и это чувствуется во всём, что они делают: качество, идея и характер в каждой детали

🛒 За атмосферой в <b>The Old Biscuit Mill</b> (Woodstock) или <b>Mojo Market</b> (Sea Point).
За шопингом <b>V&A Waterfront</b>, <b>Canal Walk</b>, <b>Cavendish Square</b>

🧵 А если хочешь уникальное загляните в путеводитель"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_shop_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_shop_ikb(),
            parse_mode="HTML")

@router.callback_query(F.data == 'routes_fri_him_bars')
async def routes_fri_him_bars(callback: types.CallbackQuery):
    
    text = """
💡 Совет от Бро Бота:
в Кейптауне культура это не экскурсия, а состояние
Главное — не пытайся всё успеть, просто идти туда, где сегодня играет музыка

Кейптаун славится своими атмосферными барами и вечеринками у океана

Здесь можно провести вечер в джаз-баре на Bree Street,пить коктейли на крыше с видом на закат в Camps Bayили танцевать под афробит до рассвета на Long Street

Любителям вина стоит заглянуть в Constantia или на винные бары в центре, а тем, кто ищет камерную атмосферу в тайные спикизи или андеграунд-клубы на Kloof Street

Более подробную подборку лучших баров, мест с живой музыкой, крафтовым пивом и заведений 18+ можно найти в <b>Путеводителе по Кейптауну</b>"""
    
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=routes_fri_him_bars_ikb(),
            parse_mode="HTML")
    except:
        await callback.message.answer(
            text,
            reply_markup=routes_fri_him_bars_ikb(),
            parse_mode="HTML")
      
