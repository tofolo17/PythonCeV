def double(a):
    return a ** 2


def triple(a):
    return a ** 3


def half(a):
    return a / 2


def increase(a, percentage):
    return a * (1 + percentage)


def decrease(a, percentage):
    return a * (1 - percentage)


def money(a):
    return str(f'R${a:.2f}').replace('.', ',')


def analysis(price, i, d):
    print(money(double(price)))
    print(money(triple(price)))
    print(money(half(price)))
    print(money(increase(price, i)))
    print(money(decrease(price, d)))
