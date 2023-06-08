from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state


from filters.EisDocNo import IsEisDocNo, IsTenderPlan2020EisDocNo
from lexicon.dictionaries import REPLIES
from keyboards.generation import create_kb
from utils.eis import Search
from FSM.groups import Add


router: Router = Router()


# Этот хэндлер сработает на комманду старт
@router.message(CommandStart())
async def command_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text='Введите реестовый номер документа')
    await state.set_state(Add.fill_eisdocno)


# Этот хэндлер сработает на комманду хэлп
@router.message(Command(commands='help', ignore_case=True))
async def command_help(msg: Message):
    await msg.answer(text=REPLIES['/help'])


# TODO Надо делать машину состояний, чтобы после выбора типа документа из словаря сразу иметь его номер в ЕИС
# Этот хэндлер сработает на корректный реестровый номер плана-графика
@router.message(IsTenderPlan2020EisDocNo())
async def get_eis_docno(msg: Message):
    # TODO Автоматически начинать поиск последней опубликованной версии
    await msg.answer(text='Это правильный номер ПГ')


# TODO Надо делать машину состояний, чтобы после выбора типа документа из словаря сразу иметь его номер в ЕИС
# Этот хэндлер сработает на корректный реестровый номер документа (кроме плана-графика)
@router.message(IsEisDocNo(), StateFilter(Add.fill_eisdocno, default_state))
async def get_eis_docno(msg: Message, state: FSMContext):
    await state.update_data(user_id=msg.from_user.id)
    await state.update_data(message_id=msg.message_id)
    await state.update_data(eisdocno=msg.text)
    dct = await state.get_data()
    await msg.reply(text=REPLIES['doctype_choose'], reply_markup=create_kb(*REPLIES['doctypes'], width=2))
    await msg.reply(text=str(dct))
    await state.set_state(Add.fill_doctype)


# Этот хэндлер сработает на извещения
@router.callback_query(Text('notification'), StateFilter(Add.fill_doctype))
async def get_notification(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(doctype='notification')
    dct = await state.get_data()
    await call.message.answer(text=f'Это проверка коллбэка {call.message.text}')
    await bot.edit_message_text(text='Wait...', chat_id=dct['user_id'], message_id=dct['message_id'] + 1)
    answ = await Search(dct['eisdocno']).get_notification_publication_date()
    await call.message.answer(text=answ)
    await call.message.answer(text=str(dct))
    await state.clear()


# Этот хэндлер сработает на протоколы
@router.callback_query()
async def get_protocol(call: CallbackQuery):
    pass


# Этот хэндлер сработает на сведения о контракте
@router.callback_query()
async def get_contract(call: CallbackQuery):
    pass


# Этот хэндлер сработает на сведения об исполнении
@router.callback_query()
async def get_contractprocedure(call: CallbackQuery):
    pass
