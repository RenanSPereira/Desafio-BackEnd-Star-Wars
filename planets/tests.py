from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .swapi_service import get_films_qty
from .models import Planet


class SWAPTests(APITestCase):

    def test_get_films_qty(self):
        response = get_films_qty('tatooine')
        self.assertEquals(response, 5)
    
    def test_get_films_qty_not_exist_planet(self):
        response = get_films_qty('null')
        self.assertEquals(response, 0)


class PlanetTests(APITestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/planets/'
        self.data = {
            'name': 'tatooine', 
            'climate': 'desert', 
            'terrain': 'Arid', 
            'films_qty': get_films_qty('tatooine')
        }
    
    def test_create_planet(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Planet.objects.get().name, 'tatooine')
        self.assertEqual(Planet.objects.get().films_qty, 5)

    def test_planet_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)