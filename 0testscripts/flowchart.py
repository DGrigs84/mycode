#!/usr/bin/env python3

print('╔══════════════════════════════════════╗')
print('║   THE MULTIPLAYER GAMING FLOWCHART   ║')
print('╠══════════════════════════════════════╣')
print('║ Note: Input \'q\' to quit at anytime!  ║')
print('╚══════════════════════════════════════╝')

def q1():
    print("\nIs real life getting in the way?")
    ans = input('\'YES\' or \'NO\'?\n  >> ')

    if ans == "yes":
        q4()
    elif ans == "no":
        q2()
    elif ans == "q":
        quit()
    else:
        print("That\'s not an option!")
        q1()

def q2():
    print("\nPlay a round!")
    print("Did you win?")
    ans = input('\'YUP\' or \'NO\'?\n  >> ')

    if ans == "yup":
        q3()
    elif ans == "no":
        print("\nYOUR TEAM NEEDS TO WIN!!")
        q1()
    elif ans == "q":
        quit()
    else:
        print("That\'s not an option!")
        q2()

def q3():
    print("\nWere you top scorer?")
    ans = input('\'YES\' or \'NO\'?\n  >> ')

    if ans == "yes":
        print("\nSweet! Do it again!")
        q1()
    elif ans == "no":
        print("\nGotta be the top scorer...or at least do better.")
        q1()
    elif ans == "q":
        quit()
    else:
        print("That\'s not an option!")
        q3()

def q4():
    print("\nHave enough time to finish a round?")
    ans = input('\'YES\' or \'NO\'?\n  >> ')

    if ans == "yes":
        q5()
    elif ans == "no":
        print("\nBetter get going! You\'re probably already late!!")
    elif ans == "q":
        quit()
    else:
        print("That\'s not an option!")
        q4()

def q5():
    print("\nYou sure?")
    ans = input('\'YES!\' or \'NO\'?\n  >> ')

    if ans == "yes!":
        q1()
    elif ans == "no":
        print("\nBetter get going! You\'re probably already late!!")
    elif ans == "q":
        quit()
    else:
        print("That\'s not an option!")
        q5()

def quit():
    print("Hasta la vista, buddy.")

if __name__ == "__main__":
    q1()
