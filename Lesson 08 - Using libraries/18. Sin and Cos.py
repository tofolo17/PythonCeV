from math import sin, cos, radians

rad = float(input('Enter an angle (degrees): '))
ang = radians(rad)

print('{:.3f} \n{:.3f}'.format(sin(ang), cos(ang)))
