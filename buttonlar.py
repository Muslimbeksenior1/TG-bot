from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from databasehaqda import rasm


def PaginationButton(count):
    buttons = InlineKeyboardBuilder()

    if count > 1:
        buttons.add(
            InlineKeyboardButton(
                text="⬅️ Orqaga",
                callback_data="orqaga"
            )
        )

    buttons.add(
        InlineKeyboardButton(
            text="❌ Ochirish",
            callback_data="shu"
        )
    )

    if count < len(rasm):
        buttons.add(
            InlineKeyboardButton(
                text="Oldinga ➡️",
                callback_data="keyingisi"
            )
        )

    return buttons.as_markup()