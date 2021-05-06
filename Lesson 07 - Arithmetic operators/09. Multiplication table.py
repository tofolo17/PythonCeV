n = int(input("Enter a number and see its multiplication table: "))

m1 = int(input("Initial multiplication number: "))
m2 = int(input("Final multiplication number: "))

i = 0
print('=' * 12)
while (m1 + i) <= m2:
    f = m1 + i
    r = n * f
    i = i + 1
    print('{} x {:2} = {}'.format(n, f, r))
print('=' * 12)
