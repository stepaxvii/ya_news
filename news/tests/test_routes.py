from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from news.models import News


class TestRoutes(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.news = News.objects.create(
            title='Заголовок',
            text='Текст'
        )

    def test_home_page(self):
        url = reverse('news:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
