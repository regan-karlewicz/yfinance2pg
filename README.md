# yfinance2pg

Download financial data to postgres database from yahoo finance.

```txt
yfinance2pg
    Download financial data to postgres database from yahoo finance.

usage:
    yfinance2pg <options>

options:
    --help
        help menu
    --exclude [value ...]
        skip download phase, possible list
        values are `companies` or `priceVolume`
    --start-date [YYYY-MM-DD]
        start date for price volume data download
        defaults to last downloaded day, or Jan 1, 1970
        if no previous data exists
    --host [string]
    --user [string]
    --dbname [string]
    --port [string]
    --password [string]
        postgres connection options
```
