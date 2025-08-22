import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # берём токен

if not TOKEN:
    raise ValueError("❌ Не найден BOT_TOKEN! Добавь его в Secrets или .env")

# Создаём объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я модератор чата 🧨")

# Главная функция запуска
async def main():
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())