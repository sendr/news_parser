from django.test import TestCase
from apps.core.models import News
from apps.api.tests import data_creator


class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.bulk_create([News(**data) for data in data_creator(400)])

    def test_get_news(self):
        news = News.objects.get(site='example345.com')
        self.assertEqual(news.author, 'Author345')

    def test_news_list(self):
        news_list = News.objects.all()
        self.assertEqual(len(news_list), 400)
