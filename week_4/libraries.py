# import random 


# # print(random.random())


# # print(random.uniform(1,10))


# print(random.randint(1,10))


import random

my_num = 18

rand_num = random.randint(1,50)

counter = 0
while my_num != rand_num:
    print(f"My number {my_num} does not equal the randomly generated number {rand_num}")
    counter +=1
    rand_num = random.randint(1,50)

print(f"The two numbers matched and it took {counter+1} times!")



