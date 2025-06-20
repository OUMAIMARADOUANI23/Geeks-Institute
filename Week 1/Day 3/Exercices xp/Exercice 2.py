class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 60)

print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

def compare_dogs_size(davids_dog,sarahs_dog):
    if davids_dog.height>sarahs_dog.height:
        print("David dog winner")
    else:
        print("Sarah dog winner")
compare_dogs_size(davids_dog,sarahs_dog)
    
    
