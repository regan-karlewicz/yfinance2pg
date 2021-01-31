def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_measurement_type(measure):
    if measure == 'Adj Close':
        return 'AdjustedClosePrice'
    if measure == 'Volume':
        return measure
    else:
        return measure + 'Price'
