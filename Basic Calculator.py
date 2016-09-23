__author__ = 'Oskar'
import time
import sys

# Basic calculator program


class CalculatorBackend():
    @staticmethod
    def add(x, y):
        print(x + y)

    @staticmethod
    def subtract(x, y):
        print(x - y)

    @staticmethod
    def multiply(x, y):
        print(x * y)

    @staticmethod
    def divide(x, y):
        print(x / y)


print("**************************")
print("**** Basic Calculator ****")
print("**************************")
print("\n"
      "This is a basic calculator \n"
      "that will allow you to add \n"
      "subtract, multiply and \n"
      "divide integers. \n")

time.sleep(1)

firstInput = int(input("Please input your first integer: "))
time.sleep(0.5)
secondInput = int(input("Please input your second integer: "))

time.sleep(0.5)
operationInput = input("Please choose one of the four operations \n"
                       "1.) Add \n"
                       "2.) Subtract \n"
                       "3.) Multiply \n"
                       "4.) Divide \n")

time.sleep(0.5)
print(firstInput, operationInput, secondInput, "Is that correct? (Y/N)")
yesOrNoInput = input()

if yesOrNoInput == "N":
    sys.exit()
elif yesOrNoInput == "Y":
    if operationInput == "Add" or "add":
        CalculatorBackend.add(firstInput, secondInput)
    elif operationInput == "Subtract" or "subtract":
        CalculatorBackend.subtract(firstInput, secondInput)
    elif operationInput == "Multiply" or "multiply":
        CalculatorBackend.multiply(firstInput, secondInput)
    elif operationInput == "Divide" or "divide":
        CalculatorBackend.divide(firstInput, secondInput)




