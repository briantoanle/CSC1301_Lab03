## Prolog
# Author: Toan Le
# Email: tle153@student.gsu.edu
# Section: 036
'''
    Purpose:
        calculate the change you are due when you buy an item in a store
    Pre-conditions (input):
        money given to the cashier(cost of item)
    Post-conditions (output):
        change user get back from the cashier(dollars, quarters, dimes, nickels and
    pennies)
'''

def main():
# Design and implementation
# 1. Output a message to identify the program, and a blank line
    print()
    print("Conversion of change to dollars, quarters, dimes, nickels and pennies")
# 2. Input amount of change from user
    amt = float(input("Enter the change amount: "))
# 3. Calculate the change to dollars, quarters, dimes, nickels and pennies

    #get amount of dollars
    dollars = int(amt / 1.0)
    #get remainder after subtracting dollars
    dollar_new = amt - dollars * 1

    #get amount of quarters
    quarters = int(dollar_new / .25)
    #get remainder after subtracting quarters and round it because I was getting long numbers
    quarter_new = round(dollar_new - quarters * .25, 2)

    #get amount of dimes
    dimes = int(quarter_new / .10)
    #get remainder after subtracting dimes and also round it
    dime_new = round(quarter_new - dimes * .10, 2)

    #get amount of nickels
    nickels = int(dime_new / .05)
    #get remainder after subtracting nickels and round it
    nickel_new = round(dime_new - nickels * .05, 2)

    #get amount pennies
    pennies = int(nickel_new / .01)


# 4. Output resulting change
    print()
    print("You will get")
    print("Dollars: ", dollars)
    print("Quarters: ", quarters)
    print("Dimes: ", dimes)
    print("Nickels: ", nickels)
    print("Pennies: ", pennies)

main()
# end of program file
# syntax error: line 19 continuing line 18 without any quotations - fix: deleted a few space and moved it to line 18
# semantics error: line 24 has to be * 100 instead of plus 100
# line 21 conversion of input type
# added dimes and nickels and pennies
# redo algorithhm after like 23