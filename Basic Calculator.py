__author__ = 'Oskar Matacz'
import time
import sys


class CalculatorMethods():
    def __init__(self, x, y, amount_of_dp):
        self.x = x
        self.y = y
        self.amount_of_dp = amount_of_dp

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

    @staticmethod
    def round(x, y):
        amount_of_dp = int(input("Please input the amount of DP you would like to round the number to: \n"))
        return round(CalculatorMethods.divide(x, y), amount_of_dp)


def calculate():
    print("**************************")
    print("**** Basic Calculator ****")
    print("**************************")
    print("\n"
          "This is a basic calculator \n"
          "that will allow you to add \n"
          "subtract, multiply and \n"
          "divide integers. \n")

    int_one = int(input("Please input your first integer: "))
    int_two = int(input("Please input your second integer: "))

    time.sleep(0.5)

    while True:
        operation_input = input("Please choose one of the four operations \n"
                                "1.) Add \n"
                                "2.) Subtract \n"
                                "3.) Multiply \n"
                                "4.) Divide \n")

        if operation_input not in {"1", "2", "3", "4"}:
            print("Please use a valid input! (1-4)\n \n")
            time.sleep(1)
        elif operation_input == "1":
            print(int_one, "+", int_two, "=", CalculatorMethods.add(int_one, int_two))
            break
        elif operation_input == "2":
            print(int_one, "-", int_two, "=", CalculatorMethods.subtract(int_one, int_two))
            break
        elif operation_input == "3":
            print(int_one, "*", int_two, "=", CalculatorMethods.multiply(int_one, int_two))
            break
        elif operation_input == "4":
            print(CalculatorMethods.round(int_one, int_two))
            break

    time.sleep(2)
    return rerun()


def rerun():
    while True:
        again = input("Thank you again for using this calculator, would you like to try again? Please type yes or no:\n")
        if again not in {"yes", "no"}:
            print("Please enter valid input!")
        elif again == "no":
            print("Thank you, bye!")
            time.sleep(1)
            sys.exit()
            break
        elif again == "yes":
            return calculate()

calculate()




