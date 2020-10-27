#/usr/bin/env python3

user = input("What's your name? ")
day = input("What day is it? ")

# Objects
print("Hello, ", user, "! Happy ", day, "!", sep="")

# Concatenation
print("Hello, " + user + "! Happy " + day + "!")
#   Can ONLY concatinate strings with strings
#     Will work:
#       print("Hello, " + user + "! Happy " + day + "!" + "123")
#     Won't Work
#       print("Hello, " + user + "! Happy " + day + "!" + 123)

# F-string
print(f"Hello, {name}! Happy {day}!")
