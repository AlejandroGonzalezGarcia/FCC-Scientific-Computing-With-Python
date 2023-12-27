class Rectangle:
    def __init__(self, width: float, height: float):
        self.name = "Rectangle"
        print(f"An instance is created {self.name}")
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width
        return self.width
    
    def set_height(self, new_height):
        self.height = new_height
        return self.height

    def get_area(self):
        return self.height * self.width

    def get_perimiter(self):
        return 2*self.height + 2*self.width
    
    def get_picture(self):
        if (self.width > 50) or self.height > 50:
            return "Too big for picture."
        height = self.height
        width = self.width

        s = ""

        for _ in range(height):
            for _ in range(width):
                s += "*"
            s += "\n"
        return s
    
    def get_amount_inside(self, shape):
        area_self = self.get_area()
        area_other = shape.get_area()
        return int(area_self / area_other)
    
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.name = "Square"
        super().__init__(side, side)
        self.side = side

    def set_side(self, new_side):
        self.side = new_side
        return  self.side

    def __repr__(self):
        return f"Square(side={self.side})"

rectangle1 = Rectangle(10,5)
rectangle2 = Rectangle(5,5)
print(rectangle1.get_amount_inside(rectangle2))
print(rectangle1)

square1 = Square(5)
print(square1.side)
print(square1.width)
print(square1.height)
square1.set_height(10)
print(square1.side)
print(square1.width)
print(square1.height)
print(square1)