import math

divisor = math.gcd(16,28)

print(divisor)

value1 = input('Enter an integer number: ')
value2 = input('Enter another integer number: ')

value1 = int(value1)
value2 = int(value2)

divisor = math.gcd(value1, value2)

print("The greatest common divisor of {0} and {1} is {2}".format(value1, value2, divisor))