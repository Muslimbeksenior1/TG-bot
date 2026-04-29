from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio

BOT_TOKEN = "8725264348:AAGbztLGWkNS8QlpHFZ-eMJ8s2NRwBH-J20"
ADMIN_ID = 7579035341  # o'zingni IDingni qo'y

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    # username bo'lmasa
    if username:
        username_text = f"@{username}"
    else:
        username_text = "yo‘q"

    text = f"""
🆕 Yangi foydalanuvchi:

👤 Ismi: {full_name}
🆔 ID: {user_id}
📛 Username: {username_text}
"""

    # profil rasm olish
    photos = await bot.get_user_profile_photos(user_id=user_id)

    if photos.total_count > 0:
        file_id = photos.photos[0][-1].file_id  # eng oxirgi (katta) rasm

        await bot.send_photo(
            chat_id=ADMIN_ID,
            photo=file_id,
            caption=text
        )
    else:
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=text + "\n📷 Profil rasmi yo‘q"
        )

    await message.answer("Xush kelibsiz ✅")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())