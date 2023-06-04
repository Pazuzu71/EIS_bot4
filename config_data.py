from dataclasses import dataclass


from environs import Env


@dataclass
class TelegramBot:
    token: str
    admin_id: int


@dataclass
class Config:
    tgbot: TelegramBot

    @staticmethod
    def load_config(path: str | None = None):
        env = Env()
        env.read_env(path=path)
        return Config(tgbot=TelegramBot(
            token=env('TOKEN'),
            admin_id=env('ADMIN_ID')
            )
        )
