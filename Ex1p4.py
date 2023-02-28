class Point:
    """Class describing 2D point"""
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        print("Вывод метода set_coords " + str(self))
        # create local attributes
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point()
pt2 = Point()

# Call method
pt.set_coords(1, 2)
Point.set_coords(pt, 1, 2)
pt2.set_coords(3, 4)

print(pt.__dict__)
print(pt2.__dict__)

print(pt.get_coords())

# get function
f = getattr(pt, 'get_coords')
print(f())