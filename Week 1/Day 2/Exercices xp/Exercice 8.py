def pizza_order():
    toppings = []
    print("Enter pizza toppings one by one. Type 'quit' to finish.")

    while True:
        topping = input("Enter a topping: ")

        if topping.lower() == 'quit':
            break

        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

    base_price = 10.0
    topping_price = 2.5
    total_price = base_price + len(toppings) * topping_price
    print("\nYour pizza will have the following toppings:")
    for t in toppings:
        print(f"- {t}")

    print(f"\nTotal cost: ${total_price:.2f}")
pizza_order()
