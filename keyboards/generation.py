from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


from lexicon.dictionaries import REPLIES


def create_kb(*buttons, width: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(*[InlineKeyboardButton(text=REPLIES.get(btn, btn), callback_data=btn) for btn in buttons], width=width)
    return builder.as_markup()
