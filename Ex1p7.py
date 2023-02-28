class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    # Method that can only work with class attributes
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(x, y))


    def get_coord(self):
        return self.x, self.y


    # Method that have no access to class or object attributes
    # We can say it's regular function inside class
    @staticmethod
    def norm2(x, y):
        return x**2 + y**2


v = Vector(3, 4)
res = v.get_coord()
res = Vector.get_coord(v)
print(res)

valid = Vector.validate(5)
print(valid)

norm = Vector.norm2(5, 11)
print(norm)