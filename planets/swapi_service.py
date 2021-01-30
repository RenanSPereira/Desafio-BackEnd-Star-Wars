import requests
import json


def get_films_qty(name):
    try:
        resp = requests.get("https://swapi.dev/api/planets/?search="+name)
        data = resp.json()

        for r in data['results']:
            films = []
            for i in r['films']:
                films.append(i)

        films_qty = len(films)
        return films_qty
    except:
        return 0