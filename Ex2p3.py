# Non data descriptor
class ReadIntX:

    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

# Data descriptor
class Integer:

    @classmethod
    def verifycoord(cls, coord):
        if type(coord) != int:
            raise TypeError("Coord nust be integer")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verifycoord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # @classmethod
    # def verifycoord(cls, coord):
    #     if type(coord) != int:
    #         raise TypeError("Coord nust be integer")

    # @property
    # def x(self):
    #     return self._x

    # @x.setter
    # def x(self, coord):
    #     self.verifycoord(coord)
    #     self._x = coord

    # @property
    # def y(self):
    #     return self._y

    # @y.setter
    # def y(self, coord):
    #     self.verifycoord(coord)
    #     self._y = coord

    # @property
    # def z(self):
    #     return self._z

    # @z.setter
    # def z(self, coord):
    #     self.verifycoord(coord)
    #     self._z = coord

p = Point3D(1, 2, 3)
print(p.__dict__)
print(p.z)
print(p.xr)