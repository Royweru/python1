class Base:
    def __int__(self, a, c):
        self.a = 'I have rights'
        self.b = 'Im the one'
        self.__c = 'and Priveledges'


class Derived(Base):
    def __int__(self):
        print(self.a)
        print(self.b)
        print(self.c)


# create an instance of the parent class

obj1 = Base()
print(obj1)
