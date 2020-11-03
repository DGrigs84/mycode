#!.usr/bin.env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# Challenge
print(f"My {challenge[2][1]}! The {challenge[2][0]}, they do {challenge[3]}!")

# Trial
print(f"My {trial[2]['goggles']}! The {trial[2]['eyes']}, they do {trial[3]}")

# Nightmare
print('My {nightmare[0]["user"]["name"]["first"]}! The {nightmare[0]["kumquat"]} do {nightmare[0]["d"]}!')
