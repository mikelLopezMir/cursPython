
first_dictionary = { "name": "John", "age": 30, "city": "New York" }
print(first_dictionary)

# rescatem valors del diccionari
print(f'El nom de la persona és {first_dictionary["name"]}')
print(f'Té {first_dictionary["age"]} anys')
print(f'I viu a {first_dictionary["city"]}')

# afegim un valor al diccionari
first_dictionary["profession"] = "developer"

# podem buscar si una de les claus està al diccionari
print("profession" in first_dictionary)

# podem buscar si un valor està al diccionari
print("developer" in first_dictionary.values())

