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
        "Хей! Рад видеть Вас в Кейптауне 🌞\n"
        "Я — <b>Бро Бот</b>, локальный помощник по всем вопросам\n"
        "По вопросам сотрудничества к @adelsuprun\n"
        "Готовы начать?"
    )
    

    if isinstance(update, types.CallbackQuery):
        await message.edit_text(
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