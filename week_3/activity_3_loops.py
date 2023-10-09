

# password = "fruitcake"

# user_entry = input("Enter your password   >   ")

# while user_entry != password:
#     print("Try again")
#     user_entry = input("Enter your password   >   ")
# else:
#     print("Correct, you have logged in successfully.")



password = "fruitcake"

user_entry1 = input("Enter your password   >   ")

while user_entry1 != password:
    print("Try again")
    user_entry2 = input("Enter your password!   >   ")
    if user_entry1 != password and user_entry2 != password:
        print("Try again!")
        user_entry3 = input("Enter your password!!   >   ")
        if user_entry1 != password and user_entry2 != password and user_entry3 != password:
            print("Login failed.")
            break
        else:
            print("Correct, you're logged in.")
            break
    else:
        print("Correct, you have logged in successfully.")
        break
        

else:
    print("Correct, you have logged in successfully.")



