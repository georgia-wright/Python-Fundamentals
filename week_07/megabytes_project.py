

order = [

]


drink_menu = {
    "Tea" : 1.00,
    "Americano" : 1.70,
    "Latte" : 1.90,
    "Cappuccino" : 1.90,
    "Mocha":2.00,
}


food_menu = {
    "X" : 120
}



total_cost = 0

drink_answer = input("Would you like to order a drink?").capitalize()

while drink_answer == "Yes":
    print(drink_menu)
    drink_item = input("Drink choice: ").capitalize()
    if drink_item in drink_menu:
        drink_quantity = int(input("How many do you want?"))
        order.append((drink_item, drink_quantity))
        drink_value = drink_menu.get(drink_item)
        drink_cost = drink_value * drink_quantity
        total_cost += drink_cost
        print(f"You have ordered {drink_quantity} x {drink_item}. The total cost is £{total_cost}")
        drink_answer = input("Would you like to order a drink?").capitalize()
    else:
        print("Sorry we don't have that item. Try again")

else:
    food_answer = input("Would you like to order food?").capitalize()
    while food_answer == "Yes":
            print(food_menu)
            food_item = input("What food would you like to order?")
            if food_item in food_menu:
                food_quantity = int(input("How many do you want?"))
                order.append((food_item, food_quantity))
                food_value = food_menu.get(food_item)
                food_cost = food_value * food_quantity
                total_cost += food_cost
                print(f"You have ordered {food_quantity} x {food_item}. The total cost is £{total_cost}")
                food_answer = input("Would you like to order food?").capitalize()
            
            else: print("Sorry we don't have that item.")
            food_answer = input("Would you like to order food?").capitalize()
    else:
        print("Checkout")

#Checkout:

print(order)
print(total_cost)

checkout_review = input("Is this order correct?").capitalize()

while checkout_review != "Yes":
        print("Please start your order again.")
        order = [
            
        ]
        

        #.....

else:
    print("Thank you for shopping with us. Please insert your card.")
    print("Here is your receipt")
    receipt = [
    
    ]
    print(receipt)
    



