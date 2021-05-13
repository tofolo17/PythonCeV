def read_money(money):
    while True:
        v = str(input(money)).strip().replace(',', '.')
        if v.replace('.', '').isnumeric():
            break
        print('Invalid.')
    return float(v)
