# Els bucles for serveixen per a repetir una acció un nombre determinat de vegades.

print("Mostraré els 5 primers valors de la taula del 7")
for i in range(5):
    print(f'7 per {i} = {7*i}')

# Range també pot fer-se servir amb un valor inicial diferent de 0

print("Mostraré més valors de la taula del 7")
for i in range(5,10):
    print(f'7 per {i} = {7*i}')

# Per últim, range pot donar-me valors incrementant-se un nombre diferent d'1

print("Mostraré els nombres parells entre 0 i 100")
for i in range(0,101,2):
    print(i)
