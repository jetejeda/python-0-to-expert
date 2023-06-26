class Phone():
    pass#Default value so that it don't throw an error.

class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.__Id = age + 1#Defining a private attribute
        self._description = 'Another way to indicate private attributes'# Not to python but to another programmer

    def __str__(self):
        return 'I am {} and this is my description'.format(self.name)
    
    def sayHello(self, message):
        return 'Hey, my name is {} and I am {} years old, you said: {}'.format(self.name, self.age, message)
    
    def __del__(self):
        print('I am {} and I just wanted to say good bye!'.format(self.name))
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

firstPhone = Phone()
print(type(firstPhone))

firstPerson = Person('Jose', 23)
print(firstPerson.sayHello('Hi!'))
print(firstPerson)
print('We used a getter method to access this attribute: ', firstPerson.description)
firstPerson.description = 'New description using setter method'
print('We used a setter method to modify this attribute: ', firstPerson.description)