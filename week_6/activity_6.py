# hide and seek
# while attempts < 5
# input name 
# variable name

# create a list of hiding places

# need time library time.sleep
# need random generator random.choice

import random

import time

hiding_places = [
    "Under the stairs",
    "Inside the wardrobe",
    "Under the bed",
    "In the garden",
    "In the attic",
    "In the pantry"
]



attempts = 0

name = input("What is your name?    ")

print(hiding_places)

hiding_spot = input("Where would you like to hide?    ").capitalize()

# print(hiding_spot)


time.sleep(1)
print("1")

time.sleep(1)
print("2")

time.sleep(1)
print("3")

time.sleep(1)
print("4")

time.sleep(1)
print("5")

time.sleep(1)
print("6")

time.sleep(1)
print("7")

time.sleep(1)
print("8")

time.sleep(1)
print("9")

time.sleep(1)
print("10")

while attempts < 5:

    guess = random.choice(hiding_places)

    print(guess)

    time.sleep(2)
    attempts += 1

    if guess == hiding_spot:
        print("I have found you!")
        break

    else:
        hiding_places.remove(guess)
        # guess = random.choice(hiding_places)
        time.sleep(2)

print("Game over! :(")





