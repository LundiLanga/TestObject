class RectProj:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def input_attributes(self):
        self.length = float(input("Enter the length:\n"))
        self.width = float(input("Enter the width:\n"))

    def output_result(self):
        print("area of a rectangle: ", self.calculate_area())
        print("perimeter of rectangle : ", self.calculate_perimeter())

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    obj = RectProj(2, 6)
    obj.output_result()
    obj.input_attributes()
    obj.output_result()
