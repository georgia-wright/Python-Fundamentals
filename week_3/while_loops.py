# answer = input("Who ordered a cortado?    >    ")

# while answer != "Alex":
#     print("This is not your drink")
#     answer = input("Who ordered a cortado?    >    ")
# else:
#     print("Enjoy your cortado, Alex")


balance = 100

amount_to_withdraw = int(input("How much?   "))

while amount_to_withdraw > balance:
    print("insufficient funds")
    amount_to_withdraw = int(input("How much?    "))
else:
    balance = balance - amount_to_withdraw
    print(f"Your new balance is {balance}")


    