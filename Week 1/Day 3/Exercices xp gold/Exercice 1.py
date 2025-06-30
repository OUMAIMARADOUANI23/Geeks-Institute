class Circle:
    def __init__(self, radius=1.0):
        self.radius=radius
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    def area(self):
        return 3.14159 * (self.radius ** 2)
    def definition(self):
        print("Un cercle est une figure géométrique dont tous les points sont à égale distance du centre.")

mon_cercle = Circle(5)
print("Périmètre :", mon_cercle.perimeter())
print("Surface :", mon_cercle.area())
mon_cercle.definition()