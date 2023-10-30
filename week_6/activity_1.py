

#lottery number generator
# random library
# create list of the numbers
# 6 numbers range 1-50

# generate 6 random numbers between 1 and 50

# ensure number doesn't appear more than once

import random

lottery_numbers = [

]

for i in range(6):
    lottery_number = random.randint(1, 50)
    while lottery_number in lottery_numbers:
        lottery_number = random.randint(1, 50)
    
    lottery_numbers.append(lottery_number)

print(lottery_numbers)







    





















