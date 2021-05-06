def lining_up():
    name = input("What's your name? ")
    print('Nice to meet you, {}!'.format(name))
    print('Nice to meet you, {:20}!'.format(name))
    print('Nice to meet you, {:>20}!'.format(name))
    print('Nice to meet you, {:<20}!'.format(name))
    print('Nice to meet you, {:^20}!'.format(name))
    print('Nice to meet you, {:=^20}!'.format(name))


def arithmetic_operators():
    n1 = float(input("1°: "))
    n2 = float(input("2°: "))
    s = n1 + n2
    sub = n1 - n2
    m = n1 * n2
    div = n1 / n2
    exp = n1 ** n2
    div_ex = n1 // n2
    rest = n1 % n2
    print(
        "Soma = {} \n"
        "Subtraçãp = {} \n"
        "Multiplicação = {} \n"
        "Divisão = {} \n"
        "Potenciação = {} \n"
        "Divisão exata = {} \n"
        "Resto = {} \n".format(s, sub, m, div, exp, div_ex, rest)
    )


# lining_up()
# arithmetic_operators()
