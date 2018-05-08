# in this tutorial you will learn how to handle exception in python

import sys
def factorial(m):
    if m <= 1 :
        return m
    else:
        return m * factorial(m-1)

print(factorial(5))

try:
   print(factorial(1000))
except RecursionError:
    print("This program calculate factorial for large number")

print("Program terminate")

# other exception example

try:
   print(5/0)
except ZeroDivisionError :
    print("exception raised in super")

############################### another example #########################

def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(0)
        finally:
            print("finally Always execute")

first_number = getint("Please Enter first number")

second_number = getint("Please Enter second number")

try:
    print(first_number/second_number)
except ZeroDivisionError:
    print("You cant divide by zero")
