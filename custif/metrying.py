#!/usr/bin/env python3

message = 'You like'


# wrap connection in a float() to accept decimals as numbers

while True:
    try:
        answer = float(input("Whats the best original Mega Man game (1-11)?\n\nThe best one is: "))
        break

    except:
        print("Choose a NUMBER dingus!")

# Trying to use the entire word, or just the number
if answer >= 12:
	message = message + ' lying. There\'s nothing higher than 11!!'
elif answer == 11:
	message = message + ' a modern take on a classic.'
elif answer == 10:
	message = message + ' the old school feel on new hardware.'
elif answer == 9:
	message = message + ' the old school feel on new hardware.'
elif answer == 8:
	message = message + '...the Playstation one..?  Really?'
elif answer == 7:
	message = message + ' having more than 2 buttons.'
elif answer == 6:
	message = message + ' it old school.'
elif answer == 5:
	message = message + ' it old school.'
elif answer == 4:
	message = message + ' it old school.'
elif answer == 3:
	message = message + ' it old school.'
elif answer == 2:
	message = message + ' it old school.'
elif answer == 1:
	message = message + ' it old school.'
elif answer == 0:
        message = message + ' a great series, but not part of the original! Try again!\n\n░░░░░░░░▄▄▄▄░░░░░░░░\n░░░░░▄███░░███▄░░░░░\n░░░▄█████▄▄█████▄░░░\n░░░██████░░██████░░░\n░░█░█▀░░▀██▀░░▀█░█░░\n░░█░█░░██░░██░░█░█░░\n░░░▀█░░▄▄▄▄▄▄░░█▀░░░\n░░░░░▀▄▄▀▀▀▀▄▄▀░░░░░'
else:
    message = message + ', didn\'t even try to answer it right. :('
print(message)
