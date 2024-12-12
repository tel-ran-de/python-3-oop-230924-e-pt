import requests
import yaml

# pip install pyyaml

def load_config():
    with open('weather.key', 'r') as file:
        config = yaml.safe_load(file)
    return config


def main():
    url = 'http://api.weatherapi.com/v1/current.json'

    key = load_config()['key']

    params = {
        'key': key,
        'q':  'Berlin',
        'aqi': 'no'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers)
    print(response.json())


if __name__ == '__main__':
    main()
