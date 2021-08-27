import os
import logging

from aiogram import Bot, Dispatcher, executor, types
import aiohttp


from config import TOKEN

# configure logging
logging.basicConfig(level=logging.INFO)

# initialize bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def auth(func):
	async def wrapper(message):
		if message['from']['id'] not in WHITELIST:
			return await message.reply('Acces Denied', reply=Flase)