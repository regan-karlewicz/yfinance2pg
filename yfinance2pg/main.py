import traceback
import time
import datetime
import math

from .db import connect, init
from .download import companies, price_volume
from .help_text import print_menu
from .args import exists, get_list, get

if exists('help'):
    print_menu()
    exit(0)

exclude = get_list('exclude')
download_companies = 'companies' not in exclude
download_price_volume = 'priceVolume' not in exclude
start_date = get('start-date')

connection_options = {
    'host': get('host'),
    'password': get('password'),
    'user': get('user'),
    'dbname': get('dbname'),
    'port': get('port')
}


def main():
    start = time.time()

    try:
        conn = connect(**connection_options)
        curs = conn.cursor()

        init(curs)
        conn.commit()

        if download_companies:
            companies(curs, conn.commit)

        if download_price_volume:
            price_volume(curs, start_date, conn.commit)

        curs.close()

        end = time.time()
        total = math.floor(end - start)
        total_time = str(datetime.timedelta(seconds=total))
        print('finished {0} h:mm:ss'.format(total_time))
    except KeyboardInterrupt:
        pass
    except Exception:
        traceback.print_exc()
    finally:
        if conn is not None:
            conn.close()
