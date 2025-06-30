class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice_level": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice_level": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice_level": "B", "gluten": True}
        ]
    def add_item(self, name, price, spice, gluten):
        new_dish = {
            "name": name,
            "price": price,
            "spice_level": spice,
            "gluten": gluten
        }
        self.menu.append(new_dish)
        print(name,"a été ajouté au menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish["price"] = price
                dish["spice_level"] = spice
                dish["gluten"] = gluten
                print(f"🔁 '{name}' a été mis à jour.")
                return
        print("Le plat",name,"n'est pas dans le menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(name,"a été supprimé du menu.")
                return
        print("Le plat",name,"n'est pas dans le menu.")

    def show_menu(self):
        print("Menu actuel :")
        for dish in self.menu:
            gluten_free = "Sans gluten" if not dish["gluten"] else "Contient du gluten"
            print(f"- {dish['name']} | {dish['price']}€ | Épices: {dish['spice_level']} | {gluten_free}")
