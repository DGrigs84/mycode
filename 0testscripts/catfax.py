#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests


## create r, which is our request object
r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## name is our iterable - meaning it will take on the values found within
    ## r.json()["all"], one after the next - which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"

def insult():
    lonely_list = []
    for name in r.json()["all"]:
        if name.get("user"):
            lonely_list.append(f'{name["user"]["name"]["first"]} {name["user"]["name"]["last"]} must be lonely to make a cat fact.')
    for x in lonely_list:
        print(x)
insult()
