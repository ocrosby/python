# [ ] Import the math module and use an appropriate function to find the greatest common divisor of 16 and 28

import math 
divisor = math.gcd(16,28)
print(divisor)

# [ ] Prompt the user to input 2 positive integers then print their greatest common divisor
int1 = input("Input a positive integer: ")
int1 = int(int1)
int2 = input("Input another positive integer:  ")
int2 = int(int2)

user_gcd = math.gcd(int1,int2)
print("The greatest common divisor of {0} and {1} is {2}".format(int1,int2,user_gcd))
