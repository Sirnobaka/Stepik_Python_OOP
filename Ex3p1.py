class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    # redefinition of __getattribute__ method
    # program calls it every time we get some attribute of Point
    def __getattribute__(self, item):
        print("__getattribute__")
        if item == 'x':
            raise ValueError('Access prohibited')
        else:
            return object.__getattribute__(self, item)

    # program calls it every time we set value of some attribute of class Point
    def __setattr__(self, key, value):
        print("__setattr__")
        if (key == 'z'):
            raise ValueError("This name is prohibited for attribute")
        else:
            return object.__setattr__(self, key, value)

    # Program calls it every time we try to get non-existing attribute of object (Point)
    # If we not redefine this method program will through AttributeError
    def __getattr__(self, item):
        #print('__getattr__: ' + item)
        return False

    # Program calls it every time we delete attribute
    def __delattr__(self, item):
        print('__delattr__: ' + item)
        # to actually delete attribute
        object.__delattr__(self, item)




pt1 = Point(1, 2)
pt2 = Point(5, 10)
# Just to show that class attributes and object attributes are not the same
print(pt1.MAX_COORD)
pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.__dict__)

# __getattribute__
a = pt1.y
print(a)

# __setattr__
pt1.y = 12

# __getattr__
print(pt1.r)
print(pt1.MAX_COORD)

# __delattr__
del pt1.x
