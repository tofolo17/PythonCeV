qKm = float(input('How many kilometers did the car run? '))
qD = int(input('What is the duration (in days) of the rental? '))

c = 60 * qD + 0.15 * qKm

print("The service costs: R${:.2f}".format(c))
