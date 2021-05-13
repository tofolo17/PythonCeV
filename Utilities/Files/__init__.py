def insert(filename, dictionary):
    file = open(filename, 'a')
    for k, v in dictionary.items():
        file.writelines(f'{k}: ')
        file.writelines(f'{v:<10}')
    file.write('\n')


def read_txt(filename):
    with open(filename, 'r') as file:
        print(file.read())
