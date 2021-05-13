def validate_options(qtd_options):
    while True:
        option = input(f'Your option: ')
        try:
            integer_option = int(option)
            if integer_option not in range(1, qtd_options + 1):
                print('Invalid.')
            else:
                break
        except ValueError:
            print('Invalid.')
    return integer_option


def validate_str(txt):
    while True:
        string_var = input(f'{txt}').title().strip()
        if type(string_var) == str and string_var.isalpha():
            return string_var
        else:
            print('Invalid.')


def validate_int(txt):
    while True:
        try:
            int_var = int(input(f'{txt}'))
            return int_var
        except Exception:
            print('Invalid.')
