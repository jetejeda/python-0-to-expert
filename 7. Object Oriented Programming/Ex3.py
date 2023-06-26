class Fabric():
    def __init__(self, location, country, value, name) -> None:
        self._location = location
        self._country = country
        self._value = value
        self._name = name
    
    def describe(self):
        return 'The factory name is {} from {} which is located in: {}'.format(self._name, self._country, self._location)
    
class carFactories(Fabric):
    def describe(self, message):
        return super().describe() + message
    
carFactory = carFactories('address', 'Guatemala', 5000000, 'Company Name')
print(carFactory.describe(' message sent using polymorphism'))