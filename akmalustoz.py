from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import asyncio
import logging
import requests

from buttons import main_menu, menu_buttons, numbers_buttons

bot = Bot(token="bot")
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

response = requests.get("https://fakeapi.pythonanywhere.com/products").json()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Botga xush kelibsiz", reply_markup=main_menu())


@dp.callback_query(F.data == "menu")
async def menu_handler(call: CallbackQuery):
    await call.message.answer_photo(
        photo="https://t4.ftcdn.net/jpg/06/04/76/33/360_F_604763387_iHshS2pHBV3JA0L909nFnSIEazs2GUfV.jpg",
        caption="Dokonimizga xush kelibsiz",
        reply_markup=menu_buttons()
    )
    await call.answer()


@dp.callback_query(F.data.startswith("product_"))
async def product_handler(call: CallbackQuery):
    title = call.data.split("product_")[1]

    for i in response:
        if i['title'] == title:
            await call.message.answer_photo(    
                photo=i['image'],
                caption=f"Summasi: {i['summ']} so'm",
                reply_markup=numbers_buttons()
            )
            break

    await call.answer()



@dp.callback_query(F.data == "back")
async def back_handler(call: CallbackQuery):
    await call.message.answer("Asosiy menyu", reply_markup=main_menu())
    await call.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
