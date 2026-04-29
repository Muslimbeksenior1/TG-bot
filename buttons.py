from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests


def main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Menyu", callback_data="menu")],
        [InlineKeyboardButton(text="Online shop", url="https://olcha.uz/oz")],
        [InlineKeyboardButton(text="Contact yuborish", callback_data="contact")],
        [InlineKeyboardButton(text="Location yuborish", callback_data="location")]
    ])
    return keyboard


def menu_buttons():
    data = requests.get("https://fakeapi.pythonanywhere.com/products").json()

    keyboard = []
    row = []

    for i in data:
        row.append(InlineKeyboardButton(
            text=i['title'],
            callback_data=f"product_{i['title']}"
        ))
        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append([InlineKeyboardButton(text="⬅️ Ortga", callback_data="back")])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def numbers_buttons():
    keyboard = []
    row = []

    for i in range(10):
        row.append(InlineKeyboardButton(text=str(i), callback_data=f"num_{i}"))
        if len(row) == 3:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append([InlineKeyboardButton(text="⬅️ Ortga", callback_data="back")])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)