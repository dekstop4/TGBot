from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

print("Бот запущен.")


# Токен бота
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на команду "/caps"
@dp.message(Command(commands=['caps']))
async def process_caps_command(message: Message):
    await message.answer(text=message.text.upper()[6:].strip())


# Этот хэндлер будет срабатывать на команду "/reverse"
@dp.message(Command(commands=['reverse']))
async def process_reverse_command(message: Message):
    await message.answer(text=message.text[:8:-1].strip())


# фильтр на капс
@dp.message(F.text.isupper())
async def dont_cry_on_my(message: Message):
    await message.answer("Не кричи на меня!😡")


# Этот хендлер срабатывает на фото
@dp.message(F.photo)
async def echo_photo(message: types.Message) -> None:
    caption = "Принято фото!"
    if message.caption:
        caption += f"\nПодпись: {message.caption}"
    await message.reply_photo(photo=message.photo[0].file_id, caption=caption)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)

print("Бот выключен.")
