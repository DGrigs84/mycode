#!/usr/bin/env python3

message = 'You like '

# wrap connection in a float() to accept decimals as numbers
answer = input("Whats the best original Mega Man game:\nMega Man 1\nMega Man 2\nMega Man 3\nMega Man 4\nMega Man 5\nMega Man 6\nMega Man 7\nMega Man 8\nMega Man 9\nMega Man 10\nMega Man 11\n\nThe best one is: ")

# Trying to use the entire word, or just the number
if answer >= 12:
    message = message + 'One that doe'
elif answer >= 5:
    message = message + 'setting video to 1080p.'
elif answer >= 2:
    message = message + 'setting video to 720p.'
else:
    message = message + ''
print(message)

