#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = (number% -10)* -1 if(number < 0) else(number%10)
if(lastdig > 5):
    print(("Last digit of {:d}" + " is {:d} ").format(number,lastdig) + "and is greater than 5")
elif(lastdig == 0):
    print(("Last digit of {:d}" + " is {:d} ").format(number,lastdig) + "and is 0")
elif(lastdig < 6 and lastdig != 0):
    print(("Last digit of {:d}" + " is {:d} ").format(number,lastdig) + "and is less than 6 and not 0")
