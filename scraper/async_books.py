import re
import requests
import locator
import aiohttp
import asyncio
import async_timeout
from bs4 import BeautifulSoup

"""
                                                            IMPORTANT!

This should make 50 requests 'simultaneously' to http://books.toscrape.com, but it doesn´t work. The code is right, the problem is
that the website does not accept 50 requests all at once and they will go one by one as if they were synchronous, 
but if you apply this code in bigger websites it will work.

"""

all_books = []


async def fetch_page(url, session):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def get_multiple_pages(*urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch_page(url, session))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()

urls = [f'http://books.toscrape.com/catalogue/page-{i + 1}.html' for i in range(50)]
pages = loop.run_until_complete(get_multiple_pages(*urls))

for page in pages:
    class BookParser:
        def __init__(self):
            self.soup = BeautifulSoup(page, 'html.parser')
            self.locator = locator.BookLocators()

        def name(self):
            book_locator = self.locator.NAME
            content = self.soup.select(book_locator)
            return [namex.attrs['title'] for namex in content]

        def rating(self):
            book_rating = self.locator.RATING
            content = self.soup.select(book_rating)
            expression = '(One|Two|Three|Four|Five)'
            matches = [re.search(expression, str(conten)) for conten in content]
            return [ratingx.group(0) for ratingx in matches]

        def price(self):
            book_price = self.locator.PRICE
            contents = self.soup.select(book_price)
            content = [content.string for content in contents]
            expression = '[0-9]*\.[0-9]*'
            matches = [re.search(expression, str(conten)) for conten in content]
            return [pricex.group(0) for pricex in matches]

        def link(self):
            book_link = self.locator.LINK
            contents = self.soup.select(book_link, href=True)
            linkz = [content.attrs['href'] for content in contents]
            link_2 = [str(l) for l in linkz]
            return [f'http://books.toscrape.com/catalogue/{l}' for l in link_2]

        def theme(self):
            book_link = self.locator.LINK
            contents = self.soup.select(book_link, href=True)
            linka = [content.attrs['href'] for content in contents]
            link_2 = [str(l) for l in linka]
            linksx = [f'http://books.toscrape.com/catalogue/{l}' for l in link_2]
            themesx = []
            for linkç in linksx:
                three = []
                page_2 = requests.get(linkç).content
                soup_2 = BeautifulSoup(page_2, 'html.parser')
                themei = soup_2.select('li a')
                three = [t.string for t in themei]
                themesx.append(three)
            return [th[2] for th in themesx]


    oi = BookParser()
    names = oi.name()
    ratings = oi.rating()
    prices = oi.price()
    links = oi.link()
    themes = oi.theme()

    for name, rating, price, link, theme in zip(names, ratings, prices, links, themes):
        all_books.append({'name': name, 'rating': rating, 'price': price, 'topic': theme, 'link': link})
