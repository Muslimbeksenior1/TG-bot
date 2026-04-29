from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

basa = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(test="Menyu",callback_data="menu", style="succes")],
        [InlineKeyboardButton(text="contackt",callback_data="contak",style="primary")]
    ]
)