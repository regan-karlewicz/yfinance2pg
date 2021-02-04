import psycopg2
import psycopg2.extras
import os

from .helpers import get_measurement_type
from .config import config


def connect(**kwargs):
    try:
        return psycopg2.connect(**kwargs)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    try:
        return connect_default()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def connect_default():
    try:
        params = config(section='postgresql')
        return psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def init(curs):
    file = open(os.path.join('schema.sql'), 'r')
    schema = file.read()
    curs.execute(schema)


def insert_symbols(curs, symbols):
    insert_query = '''
        INSERT INTO Company
        (Ticker, Name, Exchange, Industry, Sector)
        VALUES %s ON CONFLICT DO NOTHING
    '''

    psycopg2.extras.execute_values(
        curs, insert_query, symbols, template=None, page_size=100
    )


def insert_price_volume_measurement(curs, date, symbol, measure_label, value):
    m_type = get_measurement_type(measure_label)
    format_args = (m_type,) * 3
    insert_query = '''
        INSERT INTO PriceVolume
        (Ticker, Day, {})
        VALUES (%s, %s, %s)
        ON CONFLICT (Ticker, Day) DO UPDATE
        SET Ticker=EXCLUDED.Ticker,
        Day=EXCLUDED.Day,
        {}=EXCLUDED.{}
    '''.format(*format_args)

    values = (symbol, date, value,)
    curs.execute(insert_query, values)


def get_symbols(curs):
    curs.execute('SELECT Ticker FROM Company')

    fetched = curs.fetchall()
    all_symbols = map(lambda x: x[0], fetched)
    return list(all_symbols)


def get_from_date(curs):
    curs.execute('SELECT MAX(Day) FROM PriceVolume')
    return str(curs.fetchone()[0] or '1970-01-01')
