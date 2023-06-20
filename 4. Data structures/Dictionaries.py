print('First exercise')
print('Using a dictionary with the country-capital information ask for a country and return its capital')
countryInfo = {'Guatemala':'Guatemala city', 'El Salvador': 'San Salvador', 'Honduras': 'Honduras',
               'Costa Rica': 'San Jose', 'Panama':'Panama', 'Argentina': 'Buenos Aires',
               'Colombia': 'Bogota', 'Spain':'Madrid'}

country = input('Type the country you want to look for: ').title()
capital = countryInfo.get(country)
if capital:
    print('The capital for {} is: {}'.format(country, capital))
else:
    print("We don't have the capital for ", country)
