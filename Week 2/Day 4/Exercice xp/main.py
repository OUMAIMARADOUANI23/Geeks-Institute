from menu_item import MenuItem
from menu_manager import MenuManager

item = MenuItem('Burger', 35)
item.save()

item.update('Veggie Burger', 37)

item2 = MenuManager.get_by_name('Beef Stew')
if item2:
    print(f"Found: {item2.name} at {item2.price} DH")
else:
    print("Item not found.")

print("\nAll Menu Items:")
items = MenuManager.all_items()
for i in items:
    print(f"{i.name}: {i.price} DH")

item.delete()
