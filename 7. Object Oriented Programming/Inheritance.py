class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def sayHi(self):
        print("Hey, I am {} and I'm {} years old".format(self._name, self._age))

class Doctor(Person):#The Doctor class will inherit from Person
    pass

aDoctor = Doctor('Jose', 23)

aDoctor.sayHi()