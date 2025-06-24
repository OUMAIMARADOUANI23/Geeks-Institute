family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = {}
total_cost = 0
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"Hello {name}, price the ticket is {price}")
    total[name] = price 
for price in total.values():
    total_cost += price
print("Total is: ", total_cost)
