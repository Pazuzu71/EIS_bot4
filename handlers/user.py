from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart


from filters.EisDocNo import IsEisDocNo


router: Router = Router()


@router.message(CommandStart())
async def command_start(msg: Message):
    await msg.answer(text='Введите реестовый номер документа')


@router.message(IsEisDocNo())
async def get_eis_docno(msg: Message):
    await msg.answer(text='Это правильный номер')
