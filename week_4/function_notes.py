# print("this is my functions file")



# def say_hello():
#     print("Hello")

# say_hello()

# def say_goodbye():
#     print("Goodbye")

# say_goodbye()


# def say_something(something):
#     print(f"{something}")

# say_something("Hello again") # hard coded argument
# say_something(input("what do you want to say?")) # dynamic user input


# def cash_withdrawal(amount, accnum):
#     print(f"You have withdrawn {amount} from {accnum}")

# cash_withdrawal(100, 12387968)

# cash_withdrawal(300, 2049438)

# print(amount)


# def coffee_order(size, type_of_drink):
#     print(f"You have ordered a {size} {type_of_drink}")

# coffee_order("large", "latte")

# coffee_order("small", "cappucinno")

# coffee_order("medium", "flat white")


balance = 1000

def cash_withdraw(amount, accnum):
    global balance
    print(f"You have {balance}")
    
    balance = balance - amount
    
    print(f"You are withdrawing {amount} from {accnum}")
    print(f"You now have {balance}")

cash_withdraw(20, 12345678)
cash_withdraw(30, 12345678)









