

#
#
#
def sum_series(high, low=1, step=1):
    n = (high - low)/step + 1
    s = n * ((high + low) / 2)
    # print(f'sum_series ({high}, {step}, {low}):{s}')
    return s
