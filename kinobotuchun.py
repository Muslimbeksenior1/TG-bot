import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from googletrans import Translator

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Salom! 🌍 Matn yubor, men tarjima qilib beraman.\n\n🇺🇿 ↔ 🇬🇧")

@dp.message()
async def translate_text(message: types.Message):
    text = message.text

    try:
        # tilni aniqlash
        detected = translator.detect(text)
        lang = detected.lang

        if lang == "en":
            result = translator.translate(text, dest="uz")
            await message.answer(f"🇺🇿 {result.text}")
        else:
            result = translator.translate(text, dest="en")
            await message.answer(f"🇬🇧 {result.text}")

    except:
        await message.answer("❌ Xatolik yuz berdi")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
