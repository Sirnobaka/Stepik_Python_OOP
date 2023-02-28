class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Coordinates must be int or float')

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(3, 11)
print(pt.__dict__)
print(pt.get_coord())
print(pt._Point__x, pt._Point__y)