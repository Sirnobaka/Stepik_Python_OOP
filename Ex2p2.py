class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # calls getter for example
    # a = p.old
    # or setter
    # p.old = 30
    # this attribute has higher priority so program doesn't create new propety with name 'old'
    #old = property(get_old, set_old)
    #old = property()
    #old = old.setter(set_old)
    #old = old.getter(get_old)


p = Person('Andrey', 27)
#p.set_old = 28
#print(p.get_old())
#
#print(p.old)
#p.__dict__['old'] = 'old object in p'
#p.old = 30
#print(p.old, p.__dict__)
# with decorators
del p.old
p.old = 33
print(p.old, p.__dict__)