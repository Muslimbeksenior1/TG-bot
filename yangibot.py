import asyncio
import logging
from main import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from googletrans import Translator

bot = Bot(token="8541478053:AAGuBZ5ek5g3rnF7wyzA5np3QlHTkFIVeV0")
dp = Dispatcher()
translator = Translator()

logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Salom! Matn yuboring, men uni ingliz tiliga tarjima qilaman.")

@dp.message(F.text)
async def translate_handler(message: Message):
    try:
        translated = await asyncio.to_thread(translator.translate, message.text, dest="en")
        await message.answer(translated.text)
    except Exception as e:
        logging.error(f"Error: {e}")
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass