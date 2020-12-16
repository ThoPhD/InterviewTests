class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def what_am_i(self):
        return 'Rectangle'


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def what_am_i(self):
        return 'Square'


class Cube(Square):
    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        return self.what_am_i() + ' child of ' + super(Cube, self).what_am_i()

    def family_tree_2(self):
        return self.what_am_i() + ' nephew of ' + super(Square, self).what_am_i()


if __name__ == "__main__":
    c = Cube(3)
    print(c.surface_area())
    print(c.volume())
    print(c.what_am_i())
    print(c.family_tree_2())
