from news_parser.celery import app
from bs4 import BeautifulSoup
import requests
from apps.core.models import News


@app.task
def get_news():
    def has_no_id(tag):
        return tag.name == 'td' and tag.has_attr('class') and not tag.has_attr('align')
    for page in range(100):
        site_content = requests.get('https://news.ycombinator.com/news?p={}'.format(page)).content
        news = BeautifulSoup(site_content, "html.parser")
        entries = news.find_all(has_no_id, 'title')
        for entrie in entries[:-1]:  # Last tag consists of More button
            url = entrie.find('a', 'storylink')
            title = url.string
            url = url['href']
            site = entrie.find('a', '')
            site = site['href'].split('=')[-1] if site else ''
            author = entrie.find_next('tr').find('a', 'hnuser')
            author = author.string if author else ''
            if not News.objects.filter(url=url).exists():
                News.objects.create(
                    title=title,
                    url=url,
                    author=author,
                    site=site
                )
