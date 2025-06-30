import random
class MyList:
    def __init__(self, items=None):
        if items is None:
            self.items = ['a','b','c','d','e','f','g','h','i','j']
        else:
            self.items = items

    def list_inverse(self):
        return self.items[::-1] 

    def list_sorted(self):
        return sorted(self.items) 

    def random_list(self):

        return [random.randint(1, 100) for _ in range(len(self.items))]

ma_liste = MyList()
print("Liste originale :", ma_liste.items)
print("Liste inversée :", ma_liste.list_inverse())
print("Liste triée :", ma_liste.list_sorted())
print("Liste aléatoire :", ma_liste.random_list())
