import datetime
import yfinance
import math
import multitasking
import pandas as pd

from .tickers import get_symbols
from .helpers import chunks
from .db import \
    get_symbols as get_downloaded, \
    get_from_date, \
    insert_price_volume_measurement, \
    insert_symbols


@multitasking.task
def download_company(symbol, companies):
    try:
        try:
            data = yfinance.Ticker(symbol).info
            industry = data.get('industry')
            sector = data.get('sector')
            name = data.get('longName')
        except Exception:
            industry = None
            sector = None
            name = None
        companies.append((symbol, name, 'US', industry, sector,))
    except Exception as e:
        print('Failed for {0}: {1}'.format(symbol, e))


def companies(curs, commit):
    print('== Downloading company data ==')

    symbols = get_symbols()
    downloaded = set(get_downloaded(curs))

    companies = []

    current_chunk = 0
    chunk_size = 100
    total_chunks = math.ceil(len(symbols) / chunk_size)

    for symbol_chunk in chunks(symbols, chunk_size):
        current_chunk += 1
        print(
            'Downloading chunk {0} of {1}'
            .format(current_chunk, total_chunks)
        )

        any_downloaded = False
        for symbol in symbol_chunk:
            if symbol in downloaded:
                continue

            any_downloaded = True
            download_company(symbol, companies)

        if any_downloaded:
            multitasking.wait_for_tasks()

    if len(companies) > 0:
        insert_symbols(curs, companies)
        commit()


def price_volume(curs, start_date, commit):
    print('== Downloading price volume data ==')

    symbols = get_symbols()
    start = start_date or get_from_date(curs)
    end = str(datetime.date.today())

    print('Start date: ', start)

    current_chunk = 0
    chunk_size = 100
    total_chunks = math.ceil(len(symbols) / chunk_size)

    for symbol_chunk in chunks(symbols, chunk_size):
        current_chunk += 1
        print('Downloading chunk {0} of {1}'.format(
            current_chunk, total_chunks
        ))

        data = yfinance.download(
            ' '.join(symbol_chunk),
            start=start,
            end=end
        )

        for day in data.iterrows():
            date = day[0]
            prices = day[1]

            for index, value in prices.items():
                measure, symbol = index

                if pd.isna(value):
                    continue

                insert_price_volume_measurement(
                    curs, date, symbol, measure, value
                )

            commit()
