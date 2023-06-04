from aiogram.types import Message
from aiogram import Router


from filters.EisDocNo import IsNotEisDocNo


router: Router = Router()


@router.message(IsNotEisDocNo())
async def get_eis_docno(msg: Message):
    await msg.answer(text='Это неправильный номер. Проверьте корректность данных')


@router.message()
async def echo(msg: Message):
    await msg.answer(text=msg.text)
