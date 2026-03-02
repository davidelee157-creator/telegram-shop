import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import CommandStart

TOKEN = "8255870160:AAGZHcNp_L7wTQ1wmKzzvdVV1mOp9Y3sJYI"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть магазин",
                    web_app=WebAppInfo(url="https://github.com/davidelee157-creator/telegram-shop.git")
                )
            ]
        ]
    )

    await message.answer(
        "Добро пожаловать в магазин Telegram услуг",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


asyncio.run(main())