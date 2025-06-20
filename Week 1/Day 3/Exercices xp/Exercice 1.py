class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat1 = Cat("Mimi", 6)
cat2 = Cat("Fofa", 7)
cat3 = Cat("Lolo", 8)
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print("Le chat le plus âgé est" ,oldest_cat.name, "âgé de", oldest_cat.age,"ans.")


