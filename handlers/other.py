from aiogram.types import Message
from aiogram import Router


router: Router = Router()


@router.message()
async def echo(msg: Message):
    await msg.answer(text=msg.text)
