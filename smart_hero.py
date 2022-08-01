import requests
import json

def get_id(smart_heroes: list):
    ids = []
    for smart_heroes in smart_heroes:
        url = f'https://superheroapi.com/api/2619421814940190/search/{smart_heroes}'
        response = requests.get(url)
        ids.append(response.json()['results'][0]['id'])
    return ids

def find_smart_hero(smart_heroes: tuple):
    heroes_id = get_id(smart_heroes)
    iq = 0
    for i in heroes_id:
        url = f'https://superheroapi.com/api/2619421814940190/{i}/powerstats'
        response = requests.get(url)
        data_res = response.json()
        intell = int(data_res['intelligence'])
        if intell > iq:
            iq = intell
            smart_heroes = data_res['name']
    return f'Самый умный герой "{smart_heroes}"'

if __name__ == '__main__':
    heroes_smart = ('Hulk', 'Captain America', 'Thanos')
    print(find_smart_hero(heroes_smart))