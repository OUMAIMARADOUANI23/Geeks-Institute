from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\nRestaurant Menu Editor:")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show Full Menu")
        print("(X) Exit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "X":
            print("\nFinal Restaurant Menu:")
            show_restaurant_menu()
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please try again.")

def view_item():
    name = input("Enter item name to view: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        print(f"{item.name} - {item.price} DH")
    else:
        print("Item not found.")

def add_item_to_menu():
    name = input("Enter item name: ").strip()
    try:
        price = int(input("Enter item price: "))
        item = MenuItem(name, price)
        item.save()
        print("Item was added successfully.")
    except ValueError:
        print("Invalid price entered.")

def remove_item_from_menu():
    name = input("Enter the item name to delete: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Error: Item not found.")

def update_item_from_menu():
    current_name = input("Enter current item name: ").strip()
    item = MenuManager.get_by_name(current_name)
    if item:
        try:
            new_name = input("Enter new name: ").strip()
            new_price = int(input("Enter new price: "))
            item.update(new_name, new_price)
            print("Item was updated successfully.")
        except ValueError:
            print("Invalid price entered.")
    else:
        print("Error: Item not found.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if not items:
        print("The menu is empty.")
    else:
        print("\nRestaurant Menu:")
        for item in items:
            print(f"{item.name} - {item.price} DH")

if __name__ == "__main__":
    show_user_menu()
