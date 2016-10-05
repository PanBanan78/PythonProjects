balance = int(50000)
maxWithdraw = int(250)

print("Welcome to the Bank of McAuley")
print("______________________________")
print("Your balance is: £", balance)
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
else:
    if withdrawAmountInt > 250:
        print("You can't take out more than £250 at a time.")
    elif withdrawAmountInt <= 250:
        if modulo20 == 0:
            print("Withdrawing £" + str(withdrawAmountInt), "with", withdrawAmountIntDiv20, "£20 notes.")
            newBalanceCalc = balance - withdrawAmountIntDiv20 * 20
            print("______________________________")
            print("New balance:", newBalanceCalc)
        elif modulo20 != 0:
            if modulo10 == 0:
                print("Withdrawing £" + str(withdrawAmountInt), "with", withdrawAmountIntDiv10, "£10 notes.")
                newBalanceCalc = balance - withdrawAmountIntDiv10 * 10
                print("______________________________")
                print("New balance:", newBalanceCalc)
            elif modulo10 != 0:
                print("Withdrawing £" + str(withdrawAmountInt), "with", withdrawAmountIntDiv20, "£20 notes and", modulo20Div10, "£10 notes.")
                newBalanceCalc = balance - ((withdrawAmountIntDiv20 * 20) + (modulo20Div10 * 10))
                print("______________________________")
                print("New balance:", newBalanceCalc)
