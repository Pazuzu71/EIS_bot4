import asyncio


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


from handlers import other, user
from keyboards.main_menu import set_main_menu
from utils.funcs import create_dir
from config_data import Config


TOKEN = Config.load_config().tgbot.token


async def main():

    # Создаем папку темп, если ее нет. Она будет нужна для скачиваемых и временных файлов.
    create_dir('temp')

    # инициализируем хранилище
    storage: MemoryStorage = MemoryStorage()

    # создаем экземпляры бота и диспетчера
    bot: Bot = Bot(token=TOKEN, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    # создаем главное меню
    await set_main_menu(bot)

    # подключаем роутеры
    dp.include_router(user.router)
    dp.include_router(other.router)

    # очищаем очередь апдейтов, запускаем поулинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Ошибка, остановка бота!')
