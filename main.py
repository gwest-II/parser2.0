import requests
import bs4
from fake_useragent import UserAgent


url = 'https://habr.com/ru'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
ua = UserAgent()
HEADERS = {
    'User-Agent': ua.random
}

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='lxml')
article = soup.find('article')

for article in soup.find_all('article'):
    art = article.text

    for item in KEYWORDS:
        if item.lower() in art.lower():
            link = 'https://habr.com' + article.find('a', class_='tm-article-snippet__title-link').get('href')
            data = article.find('span', class_='tm-article-snippet__datetime-published').text
            title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').text
            print(f'Ссылка: {link} '
                  f'Дата: {data} '
                  f'Название: {title}')
