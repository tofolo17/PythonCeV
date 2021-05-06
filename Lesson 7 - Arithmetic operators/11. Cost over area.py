import math

h = float(input("Enter the height of the wall (meters): "))
w = float(input("Now, its width: "))
pl = float(input("What's the price of a liter of paint? R$"))
sqm = float(input('How many square meters a liter of paint paints? '))

area = h * w
liters = math.ceil(area / sqm)
price = liters * pl

print(f"\nSquared meters: {area}\nRequired liters : {liters}\nPrice: R${price}")
