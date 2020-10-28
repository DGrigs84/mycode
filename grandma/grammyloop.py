#!/usr/bin/env python3

# For every piece of [trash] I find in your [room], I'm going to [ground you] for a week!

room= ["piece of paper","wrapper","bottle","moldy cheeseburger"]
for trash in room:
    print(f"Is that a {trash} I see?! GROUNDED!!!")

# For every [toy] I find in the [hallway] I'm going to [throw them away]!

toss= [] # empty list! we'll fill this with the names of the toys we're deleting from "hallway"

hallway= ["toy soldier", "action figure", "stretch armstrong", "bop-it"]

for toy in hallway:
    print(f"Is this your {toy}? Wrong! It's the garbage man's now.")
    toss.append(toy) # we add the name of that toy to "toss"

for x in toss: # for every name of a toy in the "toss" list...
    hallway.remove(x) # ...we remove it from the "hallway" list.

print(hallway) # this is just to confirm that the hallway list is empty

# For every [headache] I get from [programming], I need to [take a shot].


shots= []
programming= ["first","second","third","fourth"]

for headache in programming:
    print(f"Got my {programming} headache. Time for my medicine.")
    shots.append(headache)

print("Looks like I've taken" + len(shots), "since I started learning to program.")

