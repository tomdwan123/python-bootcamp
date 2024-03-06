person = { 'name': 'Tom', 'age': 20 }
print(type(person))
print(person)

person['location'] = 'Berlin'
print(person)

city = person.get('city', 'Key does not exist')
print(city)

name = person.pop('name')
print(name, person)

print(person.popitem())

del person['age']
print(person)

germany = {
    'cities': ['Hamburg', 'Berlind', 'Paris'],
    'info': { 'population': 83_000, 'people': ['Tony', 'Tom', 'Trump']}
}

print(germany['cities'][1])
print(germany['info']['people'][-1])

countries = [
    {
        'cities': ['Hamburg', 'Berlind', 'Paris'],
        'info': { 'population': 83_000, 'people': ['Tony', 'Tom', 'Trump']}
    },
    {
        'cities': ['Newyork', 'Tokyo', 'Seoul'],
        'info': { 'population': 55_000, 'people': ['Ronaldo', 'Messi', 'Rooney']}
    }
]

print(countries[0]['cities'])
print(countries[1]['info']['people'][1])

person = { 'name': 'Tom', 'age': 20 }
keys = person.keys()
print(keys)

values = person.values()
print(values)
print(list(values))

d1 = { 'a': 1, 'b': 2, 'c': 3 }
d2 = { k*2: v*2 for k, v in d1.items() }
d3 = { k.upper(): v*2 for k, v in d1.items() }
print(d1)
print(d2)
print(d3)