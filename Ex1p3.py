class Point:
    """Class describing 2D point"""
    color = 'red'
    circle = 2

# Change class attribute value
Point.color = 'black'
print(Point.color)

# Make instances of class (objects)
a = Point()
b = Point()

# Chek instances
print(type(a) == Point)
print(isinstance(a, Point))
print(a.__dict__)

# Change attribute of object (local)
a.color = 'green'
print(a.color)
print(b.color)

# Add new attribute for class
Point.type_pt = 'disc'
# or do this
setattr(Point, 'prop', 1)
print(Point.prop)
# Change attribute value
setattr(Point, 'type_pt', 'square')
print(Point.type_pt)

# Get attibut
print(getattr(Point, 'a', False))

# Delete attribute
del Point.prop

# Check if attribute exists
print(hasattr(Point, 'circle'))

# Add new attributes of object
a.x = 1
a.y = 2

b.x = 5
b.y = 4

print(Point.__doc__)