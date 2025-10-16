import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import Config
from handlers import start, events, routes
from db import Database

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()
    Database()
    
    
    dp.include_router(start.router)
    dp.include_router(events.router)
    dp.include_router(routes.router)

    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())