# yfinance2pg

Download financial data to postgres database from yahoo finance.

```txt
usage:
    yfinance2pg [options]

options:
    --help
        help menu
    --exclude [value,...]
        skip download phase, possible list
        values are `companies` or `priceVolume`
    --host [string]
    --user [string]
    --dbname [string]
    --port [string]
    --password [string]
        postgres connection options
```
