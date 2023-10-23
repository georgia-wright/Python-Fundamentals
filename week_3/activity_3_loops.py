

# password = "fruitcake"

# user_entry = input("Enter your password   >   ")

# while user_entry != password:
#     print("Try again")
#     user_entry = input("Enter your password   >   ")
# else:
#     print("Correct, you have logged in successfully.")



password = "fruitcake"

user_entry = input("Enter your password   >   ")
attempts = 1

while user_entry != password and attempts < 3:
    print("Try again")
    attempts += 1
    user_entry = input("Enter your password!   >   ")
    

else:
        if user_entry == password:
            print("You have logged in successfully.")
        
        else:
            print("You have ran out of attempts.")





