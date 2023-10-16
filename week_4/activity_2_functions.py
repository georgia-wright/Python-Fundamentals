
order_count = 0

def take_order(size, topping, base):
    global order_count
    print(f"{size} pizza with {topping} and a {base} crust.")
    order_count += 1
    print("The order count is now", order_count) 

take_order("large", "ham", "thin")

take_order("small", "mushrooms", "stuffed")

take_order(input("What size would you like?  >  "), input("What topping would you like? >  "), input ("What base would you like? (thin, stuffed or thick)  >  "))


