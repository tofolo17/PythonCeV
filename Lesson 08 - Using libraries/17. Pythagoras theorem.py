from math import hypot

fst = float(input('First side: '))
snd = float(input('Second side : '))

hip = hypot(snd, fst)

print(round(hip, 2))
