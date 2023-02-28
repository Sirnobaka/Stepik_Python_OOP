class Point:
    """Class describing 2D point"""
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        print("вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("удаление экземпляра " + str(self))

    def set_coords(self, x, y):
        print("Вывод метода set_coords " + str(self))
        # create local attributes
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point(1)
print(pt.__dict__)
pt = 0