import os
import argparse
import requests
from urllib.parse import urlsplit
from dotenv import load_dotenv

load_dotenv()

def get_args():
    parser = argparse.ArgumentParser(description='Создание коротких ссылок и подсчет кликов')
    parser.add_argument("url", help="Ваша ссылка")
    namespace = parser.parse_args()
    return namespace

def shorten_link (token, url):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {'Authorization': f'Bearer {token}'}
    params = {"long_url": url}
    response = requests.post(api_url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['link']


def count_clicks (token, url):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {'Authorization': f'Bearer {token}'}
    split_url = urlsplit(url)
    full_url = f'{api_url}/{split_url.netloc}{split_url.path}/clicks/summary'
    response = requests.get(full_url, headers=headers)
    return response.json()['total_clicks']


def is_bitlink (token, url):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    split_url = urlsplit(url)
    full_url = f'{api_url}/{split_url.netloc}{split_url.path}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(full_url, headers=headers)
    return response.ok


def main():
    token = os.environ['BITLY_TOKEN']
    args = get_args()
    input_url = args.url
    try:
        if is_bitlink(token, input_url):
            print('Количество кликов: ', count_clicks(token, input_url))
        else:
            short_url = shorten_link(token, input_url)
            print("Битлинк: ", short_url)
    except requests.exceptions.RequestException as error:
        print(error)


if __name__ == '__main__':
    main()