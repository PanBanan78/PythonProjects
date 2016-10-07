__author__ = "Oskar Matacz"
__version__ = "0.5"


def read_file(file_name):
    with open(file_name, "r") as file:
        read = file.read()
        read = int(read)
        return read


def write_file(file_name, value):
    with open(file_name, "w") as file:
        print(value, file=file)


balance = read_file("bankBalance")
print(balance)
maxWithdraw = int(250)

print("Welcome to the Bank of McAuley")
print("______________________________")
print("Your balance is: £" + str(balance))
print("\nPlease note the max withdraw amount is £250")

while True:
    withdrawAmount = input("\nPlease input the amount that you would like to withdraw: ")
    try:
        withdrawAmountInt = int(withdrawAmount)
        break
    except ValueError:
        print("Invalid input! Please try again...\n")

modulo20 = withdrawAmountInt % 20
modulo10 = withdrawAmountInt % 10

withdrawAmountIntDiv20 = int(withdrawAmountInt / 20)
withdrawAmountIntDiv10 = int(withdrawAmountInt / 10)
modulo20Div10 = int(modulo20 / 10)


if withdrawAmountInt > 250:
    print("You cannot take out more than £250 at a time...")
elif withdrawAmountInt > balance:
    print("You cannot go overdraft!")
else:
    if modulo20 == 0:
        print("Withdrawing £" + str(withdrawAmountInt), "with", withdrawAmountIntDiv20, "£20 notes.")
        newBalanceCalc = balance - withdrawAmountIntDiv20 * 20
        print("______________________________")
        print("New balance: £" + str(newBalanceCalc))
        write_file("bankBalance", newBalanceCalc)
    elif modulo20 != 0:
        if modulo10 == 0:
            print("Withdrawing £" + str(withdrawAmountInt), "with", withdrawAmountIntDiv10, "£10 notes.")
            newBalanceCalc = balance - withdrawAmountIntDiv10 * 10
            print("______________________________")
            print("New balance: £" + str(newBalanceCalc))
            write_file("bankBalance", newBalanceCalc)
        elif modulo10 != 0:
            print("Withdrawing £" + str(withdrawAmountInt), "with", withdrawAmountIntDiv20, "£20 notes and", modulo20Div10, "£10 notes.")
            newBalanceCalc = balance - ((withdrawAmountIntDiv20 * 20) + (modulo20Div10 * 10))
            print("______________________________")
            print("New balance: £" + str(newBalanceCalc))
            write_file("bankBalance", newBalanceCalc)
