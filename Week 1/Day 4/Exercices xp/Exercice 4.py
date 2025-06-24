class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member named {first_name} found.")

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(f"- {member.first_name}, Age: {member.age}")

famille = Family("Smith")
famille.born("Alice", 20)
famille.born("Bob", 16)
famille.born("Charlie", 25)

famille.check_majority("Alice")
famille.check_majority("Bob")
famille.check_majority("David")

famille.family_presentation()
