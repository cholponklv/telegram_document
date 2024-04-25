import sys
import os
import django
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F,Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state,State,StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import StateFilter
sys.path.append('/home/cholponklv/Desktop/bot/DocumentBot/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DocumentBot.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
logging.basicConfig(level=logging.INFO)

from tgbot.models import User_tg
import document1
bot = Bot(token="7060584736:AAGJbc4IBFHdhJj8m2QI0-W4BG9lYoNKK0w")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user, created = User_tg.objects.get_or_create(token=message.from_user.id,
                                                   defaults={'name': message.from_user.username})

    if created:
        await message.answer(f"{user.name}, Приветствую! Я помогу вам с заполнением документа")
    kb = [
        [
            types.KeyboardButton(text="Заполнить Документ"),
            types.KeyboardButton(text="Другое действие")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите документ"
    )
    await message.answer("Выберите действие", reply_markup=keyboard)


@dp.message(F.text.lower() == "заполнить документ")
async def document_choice(message: types.Message):
    builder = InlineKeyboardBuilder()
    b1 = types.InlineKeyboardButton(
        text="Документ1", callback_data="document1")
    b2 = types.InlineKeyboardButton(
        text="Документ2", callback_data="document2")
    b3 = types.InlineKeyboardButton(
        text="Документ3", callback_data="document3")
    b4 = types.InlineKeyboardButton(
        text="Документ4", callback_data="document4")
    builder.row(b1)
    builder.row(b2)
    builder.row(b3)
    builder.row(b4)
    await message.answer(
        "Выберите документ",
        reply_markup=builder.as_markup()
    )


async def main():
    dp.include_routers(document1.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
