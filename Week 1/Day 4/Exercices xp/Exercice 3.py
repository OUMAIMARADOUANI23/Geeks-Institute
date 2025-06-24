import random

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight!"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dogs_names = ', '.join([dog.name if isinstance(dog, Dog) else str(dog) for dog in args])
        print(f"{dogs_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet.")

my_dog = PetDog("Fido", 2, 10)
my_dog.train()                 
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

dog2 = PetDog("Rex", 4, 20)
dog2.do_a_trick()
