# take input

# if a number : cast to an integer

# if a str: make uppercase

user_input = input("What would you like to say?")


while True:

    try:
        int(user_input)
        print("Your input has been saved as an integer")
        break

    except ValueError:
        if user_input == float:
            print(int(user_input))
            print("Your input has been saved as an integer.")

        else:
            print(str(user_input).upper())
            break








