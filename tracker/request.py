import urllib.request
import json
from .models import Currency, Currency_details, Article


api_key = '******************'
news_base_url = 'https://newsapi.org/v2/everything?sources=crypto-coins-news&apiKey={}'


ct_base_url = 'https://api.coinmarketcap.com/v2/ticker/'


def all_currencies(id):

    all_currencies_url = ct_base_url

    with urllib.request.urlopen(all_currencies_url) as url:
        all_currencies_data = url.read().decode('utf-8')

        get_all_currencies = json.loads(f'''{all_currencies_data}''')

        currency_results = None

        if get_all_currencies['data']:
            currency_results = get_all_currencies['data']
            x = currency_results.values()
            # x = currency_results['1']
            print("Hello")

    return x


def all_news():

    all_news_url = news_base_url.format(api_key)

    with urllib.request.urlopen(all_news_url) as url:
        all_news_data = url.read().decode('utf-8')

        get_all_news = json.loads(f'''{all_news_data}''')

        if get_all_news['articles']:
            news_results = get_all_news['articles']

    return news_results
