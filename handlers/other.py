from aiogram.types import Message
from aiogram import Router


from filters.EisDocNo import IsNotEisDocNo


router: Router = Router()

# Этот хэндлер будет срабатывать, если введен некорректный реестровый номер документа
@router.message(IsNotEisDocNo())
async def get_eis_docno(msg: Message):
    await msg.answer(text='Это неправильный номер. Проверьте корректность данных')


# Этот хэндлер будте срабатывать, если все вышестоящие хэндлеры не сработают. Это эхо.
@router.message()
async def echo(msg: Message):
    await msg.answer(text=msg.text)
