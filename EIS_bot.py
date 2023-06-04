import asyncio


from aiogram import Bot, Dispatcher


from handlers import other, user
from keyboards.main_menu import set_main_menu
from config_data import Config


TOKEN = Config.load_config().tgbot.token


async def main():

    # создаем экземпляры бота и диспетчера
    bot: Bot = Bot(token=TOKEN, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

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
