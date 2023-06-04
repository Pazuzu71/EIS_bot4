from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart, Command


from filters.EisDocNo import IsEisDocNo, IsTenderPlan2020EisDocNo
from lexicon.dictionaries import REPLIES


router: Router = Router()


# Этот хэндлер сработает на комманду старт
@router.message(CommandStart())
async def command_start(msg: Message):
    await msg.answer(text='Введите реестовый номер документа')


# Этот хэндлер сработает на комманду хэлп
@router.message(Command(commands='help', ignore_case=True))
async def command_help(msg: Message):
    await msg.answer(text=REPLIES['/help'])


# Этот хэндлер сработает на корректный реестровый номер плана-графика
@router.message(IsTenderPlan2020EisDocNo())
async def get_eis_docno(msg: Message):
    # TODO Автоматически начинать поиск последней опубликованной версии
    await msg.answer(text='Это правильный номер ПГ')


# Этот хэндлер сработает на корректный реестровый номер документа (кроме плана-графика)
@router.message(IsEisDocNo())
async def get_eis_docno(msg: Message):
    await msg.reply(text=REPLIES['doctype_choose'])

