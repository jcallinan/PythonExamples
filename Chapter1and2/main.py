class Rectangle:
    def __init__(self, width, height):
        print("I'm initializing a new Rectangle instance.")
        self.width = width
        self.height = height

    def __del__(self):
        print('A Rectangle instance is being destroyed.')

    def calculate_area(self):
        return self.width * self.height


rectangle4 = Rectangle(143, 187)
print(rectangle4.calculate_area())


def calculateArea(width, height):
    return Rectangle(width, height).calculate_area()


rectangle = Rectangle(293, 117)

print(calculateArea(143, 187))
