from rest_framework import status
from rest_framework.test import APITestCase
from apps.core.models import News
from .serializers import NewsSerializer
import json


def data_creator(count):
    key_list = ['author', 'url', 'site', 'title']
    value_list = ['Author{}', 'http://example.com{}', 'example{}.com', 'Title{}']
    for item in range(count):
        data = {}
        for ind, key in enumerate(key_list):
            data[key] = value_list[ind].format(item)
        yield data


class AccountTests(APITestCase):

    def setUp(self):
        for data in data_creator(100):
            News.objects.create(**data)

    def test_news_list(self):
        response = self.client.get('/api/posts', format='json', follow=True)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, NewsSerializer(News.objects.all(), many=True).data)
        self.assertEqual(len(response_data), 100)

    def test_news_one(self):
        response = self.client.get('/api/posts/example455.com', format='json', follow=True)
        author = json.loads(response.content)[0]['author']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author, 'Author455')

    def test_not_allowed(self):
        post_data = {'author': 'test', 'site': 'test.com', 'url': 'http://test.com', 'title': 'Test'}
        response = self.client.post('/api/posts/', data=post_data, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
