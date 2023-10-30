# guessing game

# generate a random number between 1 and 12

# user inputs a string 'higher or lower'

#generates a new number between 1 and 12 (not the same as last one)

# if input = higher and new number > number, print correct!
# else, print incorrect and new number

import random

original_number = random.randint(1,12)

print(original_number)


guess = input("Higher or Lower?   >  ").capitalize()

# while guess != "Higher" or guess != "Lower":
#     print("Please answer Higher or Lower only.")
#     guess = input("Higher or Lower?   >  ").capitalize()
#     break


new_number = random.randint(1,12)
while new_number == original_number:
    new_number = random.randint(1,12)

print(new_number)

if guess == "Higher" and new_number > original_number:
    print("You are correct!")

elif guess == "Lower" and new_number < original_number:
    print("You are correct!")

else:
    print("Unlucky.")


