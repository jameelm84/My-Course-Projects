
import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message()
async def answer_any_type(message: types.Message):
    if message.text:
        await message.answer(text=message.text)
    elif message.sticker:
        await message.answer_sticker(sticker=message.sticker.file_id)
    elif message.photo:
        # use the image id from user
        photo_id = message.photo[-1].file_id
        # send the same image
        await message.answer_photo(photo=photo_id)
    else:
        await message.reply("An other media type was used!!! ")

@dp.message()
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())