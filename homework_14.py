class Shape:
    def draw(self):
        raise NotImplementedError

    @staticmethod
    def is_length_appropriate(length: int) -> bool:
        result = True if length > 1 else False
        return result


class Triangle(Shape):
    def __init__(self, width: int):
        if Shape.is_length_appropriate(width):
            self.width = width
        else:
            raise AttributeError("Width must be higher then 1")

    def draw(self) -> None:
        for i in range(self.width + 1):
            space_count = self.width - i
            print(' ' * space_count + '* ' * i)


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        if Shape.is_length_appropriate(width) and Shape.is_length_appropriate(height):
            self.width = width
            self.height = height
        else:
            raise AttributeError("All dimensions must be higher then 1")

    def draw(self) -> None:
        for i in range(self.height):
            for j in range(self.width):
                print("*", end=" ")
            print()


def draw_shapes(shapes: list[Shape]) -> None:
    for shape in shapes:
        if isinstance(shape, Shape):
            shape.draw()
            print()
        else:
            print(f"{shape} is not Shape instance")


list_of_shapes = [Triangle(5), Rectangle(2, 5), Rectangle(4, 3), Triangle(3), Triangle(2)]
draw_shapes(list_of_shapes)


