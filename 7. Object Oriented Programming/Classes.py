class Phone():
    pass#Default value so that it don't throw an error.

class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def sayHello(self, message):
        return 'Hey, my name is {} and I am {} years old, you said: {}'.format(self.name, self.age, message)

firstPhone = Phone()
print(type(firstPhone))

firstPerson = Person('Jose', '23')
print(firstPerson.sayHello('Hi!'))