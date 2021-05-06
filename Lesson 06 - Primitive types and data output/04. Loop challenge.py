user_input = input("Type something: ")

try:
    val = int(user_input)
    print(type(val))
except ValueError:
    try:
        val = float(user_input)
        print(type(val))
    except ValueError:
        print(type(user_input))
