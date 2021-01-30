def get(measure):
    if measure == 'Adj Close':
        return 'AdjustedClosePrice'
    if measure == 'Volume':
        return measure
    else:
        return measure + 'Price'
