from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import requests

bot = Bot(token="8637489461:AAFTjVeF1Ls9cam6RIXnzDLth8upvF1F93M")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Video link yubor (YouTube yoki Instagram)")


@dp.message(F.text)
async def download_video(message: Message):
    url = message.text

    api_url = f"https://api.vevioz.com/api/button/mp4/{url}"

    try:
        res = requests.get(api_url)

        if res.status_code == 200:
            await message.answer(
                "Yuklash uchun shu linkni och:\n" + api_url
            )
        else:
            await message.answer("Xatolik yuz berdi")
    except:
        await message.answer("Link noto‘g‘ri yoki ishlamayapti")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())