import datetime
import time
import aiohttp


class Search:

    def __init__(self, eisdocno: str):
        self.eisdocno = eisdocno

    async def get_notification_publication_date(self):

        async with aiohttp.ClientSession() as session:
            time.sleep(1)
            url = f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={self.eisdocno}'
            # url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=0166300020623000027'
            async with session.get(url) as response:
                html = await response.text()
                status = response.status
                print(type(html), html)
        return status

    async def get_protocol_publication_date(self):
        pass

    async def get_contract_publication_date(self):
        pass

    async def get_contractprocedure_publication_date(self):
        pass
