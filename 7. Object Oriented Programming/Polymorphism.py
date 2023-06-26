class Animals():
    def __init__(self, age, name):
        self._age = age
        self._name = name

    def walk(self):
        print("I'm a {} and I can walk!".format(self._name))
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

class Dog(Animals):
    def walk(self):
        print('I can walk with 4 legs')

class Kangaroo(Animals):
    def walk(self):
        print('I can walk with 2 legs')

myDog = Dog(5, 'Koda')
myDog.walk()
myKangaroo = Kangaroo(10, 'Jack')
myKangaroo.walk()