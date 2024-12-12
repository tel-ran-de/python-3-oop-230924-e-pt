# Выполнить запрос и получить текущие координаты МКС и состав экипажа
# вывести результаты в понятном для человека виде
# сайт с информацией http://api.open-notify.org

import requests
import json
import datetime


def main():
    url_coord = 'http://api.open-notify.org/iss-now.json'
    coord_response = requests.get(url_coord)
    coords = json.loads(coord_response.text)
    longitude = coords['iss_position']['longitude']
    latitude = coords['iss_position']['latitude']
    date_time = datetime.datetime.fromtimestamp(coords['timestamp'])
    message = coords['message']

    url_team = 'http://api.open-notify.org/astros.json'
    team_response = requests.get(url_team)
    team = json.loads(team_response.text)
    people = team['people']

    print(f'date: {date_time.date()}, time: {date_time.time()}, \nlongitude: {longitude}, latitude: {latitude}')
    for person in people:
        print(f'Craft: {person["craft"]} name: {person["name"]}')


if __name__ == '__main__':
    main()
