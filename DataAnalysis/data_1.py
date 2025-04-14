import math


class Point3D:
    """
    This class describes 3D dots in some space.
    """

    __name = "Dots"

    @classmethod
    def verify_data(csl, a):
        if isinstance(a, (int, float)):
            return a
        else:
            raise TypeError("Coordinates must be integer!")

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = self.verify_data(x)
        self.y = self.verify_data(y)
        self.z = self.verify_data(z)

    def vector(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):

        return (
            self.x == other.x and
            self.y == other.y and
            self.z == other.z
        )

    @staticmethod
    def vector2(x, y, z):
        return math.sqrt(x**2+y**2+z**2)

    def __bool__(self):
        return Point3D.vector2(self.x, self.y, self.z)

    @classmethod
    def data_vector(cls, other):
        if not isinstance(other, (tuple, list, Point3D)):
            raise ArithmeticError("Right operator in not allowed type!")
        return other if isinstance(
            other, (tuple, list)) else Point3D.vector2(other.x, other.y, other.z)

    def __ge__(self, other):
        right_operator = self.data_vector(other)
        return Point3D.vector2(self.x, self.y, self.z) >= right_operator if isinstance(other, Point3D) else Point3D.vector2(self.x, self.y, self.z) >= Point3D.vector2(other[0], other[1], other[2])

    def __lt__(self, other):
        right_operator = self.data_vector(other)
        return Point3D.vector2(self.x, self.y, self.z) >= right_operator if isinstance(other, Point3D) else Point3D.vector2(self.x, self.y, self.z) < Point3D.vector2(other[0], other[1], other[2])

    @staticmethod
    def show_vector(result):
        return result if isinstance(result, (float, int)) else Point3D.vector(result)

    def __add__(self, other):
        right_operator = self.data_vector(other)
        return Point3D(Point3D.vector(self) + right_operator) if isinstance(other, Point3D) else Point3D.vector2(self.x, self.y, self.z) + Point3D.vector2(other[0], other[1], other[2])

    def __radd__(self, other):
        return self.__add__(other)  # Делегируем работу в __add__



class ColorPoint3D(Point3D):

    def __init__(self, x, y, z, fill = None):
        super().__init__(x, y, z)
        self.fill = 'red'

    def vector(self):
        print('Color Vector')
        return super().vector()

class BlackPoint3D(Point3D):

    def __init__(self, x, y, z, fill = 'Black'):
        super().__init__(x, y, z)
        self.fill = fill

    def vector(self):
        print('Black Vector')
        return super().vector()


try:
    d1 = Point3D(3, 0, 0)
    d2 = ColorPoint3D(12, 3, 3)
    d3 = BlackPoint3D(12, 3, 3)
    print(d1.vector())
    print(d2.vector())
    print(BlackPoint3D.vector(d1))
except TypeError as e:
    print(e)
except ArithmeticError as e:
    print(e)
