import requests

endpoint = 'https://www.sec.gov/include/ticker.txt'


def get_symbols():
    tickers = []

    r = requests.get(endpoint)

    for line in r.text.split('\n'):
        tickers.append(line.split('\t')[0].upper())

    return tickers
