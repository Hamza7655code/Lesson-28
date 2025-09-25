class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)

    def perimeter(self):
        print("Perimeter:", 2 * 3.14 * self.radius)

r = float(input("Enter radius: "))
c = Circle(r)

c.area()
c.perimeter()
