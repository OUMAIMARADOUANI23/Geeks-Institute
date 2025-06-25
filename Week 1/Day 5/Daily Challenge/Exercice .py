import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area():.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return math.isclose(self.radius, other.radius)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    def draw(self, pen):
        pen.penup()
        pen.forward(self.radius)
        pen.pendown()
        pen.circle(self.radius)
        pen.penup()
        pen.backward(self.radius)
        pen.pendown()

def draw_circles(circles):
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()

    for circle in circles:
        circle.draw(pen)
        pen.penup()
        pen.forward(circle.diameter + 20)
        pen.pendown()

    screen.mainloop()

c1 = Circle(radius=30)
c2 = Circle(diameter=100)
c3 = Circle(radius=15)
c4 = Circle(radius=50)

liste = [c1, c2, c3, c4]
liste.sort() 

print("Cercles triés:")
for c in liste:
    print(c)

draw_circles(liste)
