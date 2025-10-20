from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.inline import start_menu

router = Router()

@router.message(Command('start'))
@router.callback_query(F.data == 'start')
async def cmd_start(update: types.Message | types.CallbackQuery):
    if isinstance(update, types.CallbackQuery):
        message = update.message
        await update.answer()
    else:
        message = update
    
    text = (
        "Я помогу разобраться с городом — от жилья и транспорта до мероприятий и крутых мест\n\nЧто интересует первым делом?"
    )
    

    if isinstance(update, types.CallbackQuery):
        try:
            await message.edit_text(
                text,
                reply_markup=start_menu(),
                parse_mode="HTML"
            )
        except Exception:
            await message.delete()
            await message.answer(
                text,
                reply_markup=start_menu(),
                parse_mode="HTML"
        )
    else:
        await message.answer(
            text,
            reply_markup=start_menu(),
            parse_mode="HTML"
        )