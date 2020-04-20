import datetime
import bs4
import requests
from collections import namedtuple
import urllib.parse
from telebot import types, TeleBot
import telebot
import config

bot: TeleBot = telebot.TeleBot(config.TOKEN)
InnerBlock = namedtuple('Block', 'title, price,currency,date,url') #Делим строки

class Block(InnerBlock):

    def __str__(self):
        return f'Название: {self.title}\nЗарплата: {self.price}{self.currency}\t\nДата размерещения: {self.date}\t\nСсылка: {self.url}'


class AvitoParser:

    def __init__(self): #Чтобы не распознали, что мы боты
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def get_page(self, page: int = None): # ПРоверяем адрес страницы и так же указываем ссылку на страницу
        params = {
            'cd': 1,
            'radius': 0,
        }
        if page and page > 1:
            params ['p'] = page
        url = 'https://www.avito.ru/moskva/avtomobili/audi/a7'
        url = 'https://www.avito.ru/staryy_oskol/vakansii'
        #url = 'https://www.avito.ru/moskva/avtomobili/audi/a7-ASgBAgICAkTgtg3elyjitg3snSg'
        r = self.session.get(url, params = params)
        return r.text

    @staticmethod #Сортируем дату которая имеется
    def parse_date(item: str):
        params = item.strip().split(' ')

        if len(params) == 2:
            day, time = params
            if day == 'Сегодня':
                date = datetime.date.today()
            elif day == 'Вчера':
                date = datetime.date.today() - datetime.timedelta(days=1)
            else:
                print('Не смогли разобрать день: ', item)
                return
            time = datetime.datetime.strptime(time, '%H:%M').time()
            return datetime.datetime.combine(date=date, time=time)
        elif len(params) == 3:
            day, month_hru, time = params
            day = int(day)
            months_map ={
                'январь': 1,
                'февраль': 2,
                'апреля': 4,
                'мая': 5,
                'июня': 6,
                'июля': 7,
                'августа': 8,
                'сентября': 9,
                'октября': 10,
                'марта': 3,
                'ноября': 11,
                'декабря': 12,
            }
            month = months_map.get(month_hru)
            if not month:
                print('Ноу', item)
                return

            today = datetime.datetime.today()
            time = datetime.datetime.strptime(time, '%H:%M')

            return datetime.datetime(day = day, month = month, year = today.year, hour= time.hour, minute =time.minute)

    def parse_block(self, item): #переходим на нужный сайт
        url_block = item.select_one('a.snippet-link')
        # print(url_block)
        # return
        href = url_block.get('href')
        if href:
            url = 'https://www.avito.ru' + href
        else:
            url = None

        title_block=item.select_one('h3.snippet-title a') #Тут указываем блок с текстом
        title = title_block.string.strip()

        price_block = item.select_one('span.snippet-price ') #Тут указываем блок с ценой
        price_block = price_block.get_text('\n')
        #price_block = price_block.string.strip()
        price_block = list(filter(None,  map(lambda i: i.strip(), price_block.split(' '))))

        if len(price_block) == 4 or len(price_block) == 3 :  #Если длина денег
            price = price_block[:3]
            price = ' '.join(price)
            currency = price_block[-1]
            #two = price[:-1]
            #result = [map(i) for i in two.split()]
            #print(two)
            #return
        else:
            price, currency = None, None
            print('Что то пошло не так при поиске цены: ', price_block)
        # print(price, currency)
        # return


        date = None
        date_block = item.select_one('div.snippet-date-row div.snippet-date-info') #Так же блок с датой
        absolute_date = date_block.get('data-tooltip') #блок с датой в формате

        if absolute_date:
            date = self.parse_date(item=absolute_date)

        return Block(
            url = url,
            title = title,
            price = price,
            currency = currency,
            date = date,
        )
    def get_pagination_limit(self): #Узнаем кол-во страниц
        text = self.get_page()
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('a.pagination-page')

        last_button = container[-1]

        href = last_button.get('href')
        if not href:
            return 1
        r = urllib.parse.urlparse(href)

        params = urllib.parse.parse_qs(r.query)
        return int(params['p'][0])


    def get_block(self, page: int = None): #Основной цикл где все происходит
        text = self.get_page(page=page)
        #print(text)
        #return
        soup = bs4.BeautifulSoup(text, 'lxml')

        container = soup.select('div.snippet-horizontal.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        #container = soup.select('div.item.item_table.clearfix.js-catalog-item.enum.item-with-contact.js-item-extended')
        for item in container:
                block = self.parse_block(item = item)
                print(block)
                with open('../Python/text.data', 'a', encoding ='utf-8') as f:
                    f.write(str(block) + '\n')


    def parse_all(self):
        limit = self.get_pagination_limit()
        print(f'Всего страниц: {limit}')
        for i in range(1, limit + 1):
            self.get_block(page=i)
def main():

        p = AvitoParser()
        p.parse_all()
        #a = p.get_block()
       # p.get_pagination_limit()
if __name__ == '__main__':
    main()