# function def

# parameters : integer 1, integer 2

# generate 6 random numbers - for i in range(6)
#random.randint(int 1, int 2)

#sort in order highest to lowest

#print the numbers

import random



def random_generator(integer_1, integer_2):
    
    random_list = [
        
    ]

    for i in range(6):
        random_list.append(random.randint(integer_1, integer_2))

    random_list.sort(reverse=True)

    print(random_list)

random_generator(int(input("Input your first number")), int(input("Input your second number.")))

    






