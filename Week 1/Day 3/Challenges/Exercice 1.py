class Farm:
    def __init__(self, farm_name):
        self.farm_name=farm_name
        self.name=farm_name
        self.animals={}
    def add_animal(self, animal_type ,count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    def get_info(self):
            output = f"{self.name}'s farm\n\n"
            for animal, count in self.animals.items():
                output += f"{animal:<10} : {count}\n"
            output += "\n    E-I-E-I-0!"
            return output
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

def get_animal_types(self):
        return sorted(self.animals.keys())

def get_short_info(self):
        animals = self.get_animal_types()
        phrases = []

        for animal in animals:
            name = animal
            if self.animals[animal] > 1:
                if name.endswith("y"):
                    name = name[:-1] + "ies" 
                elif name.endswith("s"):
                    name = name 
                else:
                    name += "s"
            phrases.append(name)

        animal_list = ", ".join(phrases[:-1])
        if len(phrases) > 1:
            animal_list += f" and {phrases[-1]}"
        else:
            animal_list = phrases[0]

        return f"The {self.name} farm has {animal_list}."
