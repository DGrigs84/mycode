#!/usr/bin/env python3


x = float(input("Whats your first number?: "))
y = float(input("What will you add to it?: "))

# Add values of x and y
def add_calc(x,y):
    print("So, " + str(x) + " + " + str(y) + " =", (x+y))

add_calc(x,y)

# Subtract values of x and y
def sub_calc(x,y):
    print("So, " + str(x) + " - " + str(y) + " =", (x-y))

sub_calc(x,y)

# Multiply values of x and y
def mult_calc(x,y):
    print("So, " + str(x) + " * " + str(y) + " =", (x*y))

mult_calc(x,y)

# Divide the value of y from x
def div_calc(x,y):
    print("So, " + str(x) + " / " + str(y) + " =", (x/y))

div_calc(x,y)

