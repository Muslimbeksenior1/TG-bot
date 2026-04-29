import asyncio
import logging
from aiogram import Bot, Dispatcher,types



from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token="")


dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("salom")

async def main():
    await bot.send_message(chat_id=7579035341, text = "bot ishladi")
    await dp.start_polling(bot)
if __name__ == "__sadaa__":
    try:
        asyncio.run(sadaa())
    except:
        print('tugadi')
