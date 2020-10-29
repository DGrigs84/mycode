#!/usr/bin/env python3

# Let's user know what the purpose of this script is
print("We\'re going to do some math with two values!\n")

# Add values of x and y
#def add_calc(x,y):
#    print("\nSo, " + str(x) + " + " + str(y) + " =", (x+y))

# User will input the values
x = float(input("What\'s your first number?: "))
y = float(input("What\'s the second number?: "))

# User is informed of the next step
print("\nWhat would you like to do with these values?\n")

# Lists the options for the user to choose from
print("1. Let\'s ADD \'em!\n2. Let\'s SUBTRACT \'em!\n3. Let\'s MULTIPLY \'em!\n4. Let\'s DIVIDE \'em!\n")

# Add values of x and y
def add_calc(x,y):
    print("\nSo, " + str(x) + " + " + str(y) + " =", (x+y))

# Subtract values of x and y
def sub_calc(x,y):
    print("\nSo, " + str(x) + " - " + str(y) + " =", (x-y))

# Multiply values of x and y
def mult_calc(x,y):
    print("\nSo, " + str(x) + " * " + str(y) + " =", (x*y))

# Divide the value of y from x
def div_calc(x,y):
    print("\nSo, " + str(x) + " / " + str(y) + " =", (x/y))

choice = input("Hmm... I choose... ")
if choice == str(1):
    add_calc(x,y)

elif choice == str(2):
    sub_calc(x,y)

elif choice == str(3):
    mult_calc(x,y)

elif choice == str(4):
    div_calc(x,y)

else: print("That's not one of the choices ya dingus!!!")
