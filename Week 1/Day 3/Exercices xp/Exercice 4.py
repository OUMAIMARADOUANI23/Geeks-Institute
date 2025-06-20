class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animal_groups = {}
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} est déjà dans le zoo.")
    def get_animals(self):
        print("Animaux dans le zoo :")
        for animal in self.animals:
            print(animal)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu.")
        else:
            print(f"{animal_sold} n'est pas dans le zoo.")
    def sort_animals(self):
        self.animal_groups = {}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            if first_letter not in self.animal_groups:
                self.animal_groups[first_letter] = []
            self.animal_groups[first_letter].append(animal)
        return self.animal_groups
    def get_groups(self):
        if not self.animal_groups:
            self.sort_animals()
        print("Groupes d'animaux :")
        for letter, group in self.animal_groups.items():
            print(f"{letter}: {group}")

            
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()

