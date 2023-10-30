# # take input

# # if a number : cast to an integer

# # if a str: make uppercase

# user_input = input("What would you like to say?")


# while True:

#     try:
#         int(user_input)
#         print("Your input has been saved as an integer")
#         break

#     except ValueError:
#         if user_input == float:
#             print(int(user_input))
#             print("Your input has been saved as an integer.")

#         else:
#             print(str(user_input).upper())
#             break







x = input("Put here")
y = x.replace(".", "")


print(y)

print(x.isdigit())

print(y.isdigit())


if x.isdigit() == False and y.isdigit() == True:
    answer = float(x)
    print("Floating number found.")

elif x.isdigit() == True:
    answer = int(x)
    print("Integer number found.")

else:
    answer = x
    print("This is a string.")

print(answer)


# using the .isdigit allows us to test if the value is a digit string or not. 
# if it is, it is an integer. If it isn't, it can either be a float or a string

# we can remove the decimal place using .replace
# from there we can test if the new variable without a decimal point is a digit string.
# if this new test comes back as true, we know the original value was a floating point.

















