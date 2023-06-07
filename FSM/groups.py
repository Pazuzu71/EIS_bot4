from aiogram.filters.state import State, StatesGroup


class Add(StatesGroup):
    fill_eisdocno = State()
    fill_doctype = State()
