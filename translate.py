from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

API_TOKEN = "8541478053:AAGuBZ5ek5g3rnF7wyzA5np3QlHTkFIVeV0"

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


class ProfileForm(StatesGroup):
    xodim = State()
    yosh = State()
    texnologiya = State()
    telegram = State()
    hudud = State()
    narxi = State()
    kasbi = State()
    murojaat_vaqti = State()
    maqsad = State()


questions = [
    ("👨‍💼", "kasb"),
    ("🕑", "Yosh"),
    ("📚", "nimalarni bilasiz"),
    ("🇺🇿", "Telegram @name"),
    ("🌐", "Hudud"),
    ("💰", "qancha oylik bilan ishlamoqchisiz"),
    ("👨🏻‍💻", "hohishingiz"),
    ("🕰", "Murojaat qilish vaqti"),
    ("🔎", "maqsadingiz"),
]


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(ProfileForm.xodim)
    await message.answer(f"{questions[0][0]} {questions[0][1]}:")


@dp.message(ProfileForm.xodim)
async def process_xodim(message: types.Message, state: FSMContext):
    await state.update_data(xodim=message.text)
    await state.set_state(ProfileForm.yosh)
    await message.answer(f"{questions[1][0]} {questions[1][1]}:")


@dp.message(ProfileForm.yosh)
async def process_yosh(message: types.Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await state.set_state(ProfileForm.texnologiya)
    await message.answer(f"{questions[2][0]} {questions[2][1]}:")


@dp.message(ProfileForm.texnologiya)
async def process_texnologiya(message: types.Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    await state.set_state(ProfileForm.telegram)
    await message.answer(f"{questions[3][0]} {questions[3][1]}:")


@dp.message(ProfileForm.telegram)
async def process_telegram(message: types.Message, state: FSMContext):
    await state.update_data(telegram=message.text)
    await state.set_state(ProfileForm.hudud)
    await message.answer(f"{questions[4][0]} {questions[4][1]}:")


@dp.message(ProfileForm.hudud)
async def process_hudud(message: types.Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(ProfileForm.narxi)
    await message.answer(f"{questions[5][0]} {questions[5][1]}:")


@dp.message(ProfileForm.narxi)
async def process_narxi(message: types.Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await state.set_state(ProfileForm.kasbi)
    await message.answer(f"{questions[6][0]} {questions[6][1]}:")


@dp.message(ProfileForm.kasbi)
async def process_kasbi(message: types.Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await state.set_state(ProfileForm.murojaat_vaqti)
    await message.answer(f"{questions[7][0]} {questions[7][1]}:")


@dp.message(ProfileForm.murojaat_vaqti)
async def process_murojaat_vaqti(message: types.Message, state: FSMContext):
    await state.update_data(murojaat_vaqti=message.text)
    await state.set_state(ProfileForm.maqsad)
    await message.answer(f"{questions[8][0]} {questions[8][1]}:")


@dp.message(ProfileForm.maqsad)
async def process_maqsad(message: types.Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    
    data = await state.get_data()
    
    result = (
        f"👨‍💼 kasbingiz: {data.get('kasbingiz', '')}\n"
        f"🕑 Yosh: {data.get('yosh', '')}\n"
        f"📚 bilish darajangiz nimalar bilishingiz: {data.get('nimalarni bilish', '')}\n"
        f"🇺🇿 Telegram: {data.get('telegram', '')}\n"
        f"🌐 Hudud: {data.get('hudud', '')}\n"
        f"💰 Narxi: {data.get('narxi', '')}\n"
        f"👨🏻‍💻 Kasbi: {data.get('kasbi', '')}\n"
        f"🕰 Murojaat qilish vaqti: {data.get('murojaat_vaqti', '')}\n"
        f"🔎 Maqsad: {data.get('maqsad', '')}"
    )
    
    await message.answer(result)
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())