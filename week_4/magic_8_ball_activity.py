# good list and bad list - will need square brackets and name for lists

# will need input - What question would you like to ask?

# will need to use random library in order to generate a random integer (1-8)

# if function to decipher whether number is odd or even
# if number is  2, 4, 6 or 8, -> good fortune
# if not (!=) , bad fortune.

#then random method to pick out of good or bad list (random index number, 0-3)

# use colorama on the print of each answer

import random
import time 
from colorama import Back, Fore, Style


good_list = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely"]


bad_list = [
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good"]


user_question = input("What is your question?    ")

time.sleep(5)

random_number = random.randint(1,8)

# print(random_number)

if random_number == 2 or random_number == 4 or random_number == 6 or random_number == 8:
    # good_choice = random.randint(0,3)
    print(Fore.GREEN + (good_list[random.randint(1,3)]))
else:
    print(Fore.RED + (bad_list[random.randint(1,3)]))

    








