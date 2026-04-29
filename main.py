import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from buttonlar import PaginationButton
from databasehaqda import rasm

logging.basicConfig(level=logging.INFO)

bot = Bot(token="8541478053:AAGuBZ5ek5g3rnF7wyzA5np3QlHTkFIVeV0")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    count = 1

    await message.answer_photo(
        photo=rasm[count - 1],
        caption=f"Rasm {count}/{len(rasm)}",
        reply_markup=PaginationButton(count)
    )


@dp.callback_query(F.data == "keyingisi")
async def next_photo(callback: types.CallbackQuery):
    count = int(callback.message.caption.split("/")[0].split()[-1]) + 1

    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=rasm[count - 1],
            caption=f"Rasm {count}/{len(rasm)}"
        ),
        reply_markup=PaginationButton(count)
    )

    await callback.answer()


@dp.callback_query(F.data == "orqaga")
async def prev_photo(callback: types.CallbackQuery):
    count = int(callback.message.caption.split("/")[0].split()[-1]) - 1

    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=rasm[count - 1],
            caption=f"Rasm {count}/{len(rasm)}"
        ),
        reply_markup=PaginationButton(count)
    )

    await callback.answer()


@dp.callback_query(F.data == "shu")
async def delete_message(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())