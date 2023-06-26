class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def sayHi(self):
        print("Hey, I am {} and I'm {} years old".format(self._name, self._age))

class Doctor(Person):#The Doctor class will inherit from Person
    def __init__(self, name, age, specialization):
        super().__init__(name, age)##Inherit all the attributes defined in the init of the parent class (Person)
        self._specialization = specialization

    @property
    def specialization(self):
        return self._specialization

aDoctor = Doctor('Jose', 23, 'Cardiology')

aDoctor.sayHi()
print(aDoctor.specialization)