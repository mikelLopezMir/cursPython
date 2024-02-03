# Podem demanar a l'usuari la introducció d'un valor
name = input("Si us plau, introduiu el vostre nom:\n")
print(f'Hola, {name or "persona desconeguda"}, benvingut a Python!')
