# Primites types
def p_types():
    n1 = int(input("Int number: "))
    n2 = float(input("Float number: "))

    print("Is the first number higher than the second?")

    if bool(n1 > n2):
        msg = str("Yes, it is!")
    else:
        msg = str("No, it isn't.")
    print(msg)


# Printing
def printing():
    s = int(input("Enter an integer: "))

    print("You typed", s)
    print('You typed {}'.format(s))
    print(f'You typed {s}')

    print(type(s))


# Some methods
def bool_methods():
    n = input('Type something: ')

    print(n.isnumeric())
    print(n.isalpha())
    print(n.isalnum())

# p_types()
# printing()
# bool_methods()
