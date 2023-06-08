import datetime
import time
import aiohttp
from bs4 import BeautifulSoup


class Search:

    def __init__(self, eisdocno: str):
        self.eisdocno = eisdocno

    @staticmethod
    def no_result(soup: BeautifulSoup):
        """Этот метод проверяет в найденом супе наличие записей"""
        return soup.find('p', class_="noRecords")

    async def get_notification_publication_date(self):

        async with aiohttp.ClientSession() as session:
            # Таймаут нужен, чтобы успела прокинуться сессия. Иначе 404.
            time.sleep(1)
            # Параметры подключения: хэдерс и урл
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                          'q=0.8,application/signed-exchange;v=b3;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/101.0.4951.54 Safari/537.36'
            }
            url = f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={self.eisdocno}'
            # Сначала проверяем наличие документа в поиске ЕИС. Суп поиска ЕИС берем сразу без сохранения в файл.
            async with session.get(url=url, headers=headers) as response:
                soup_search = BeautifulSoup(await response.text(), 'lxml')
            if self.no_result(soup_search):
                return "Поиск не дал результатов"

        return "Поиск дал результат"

    async def get_protocol_publication_date(self):
        pass

    async def get_contract_publication_date(self):
        pass

    async def get_contractprocedure_publication_date(self):
        pass
