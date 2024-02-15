# El while està pensat per quan no tenim clar quantes vegades
# es repetirà una acció, encara que també es pot fer servir
# per a quan si ho coneixem.
# Comencem per una acció que es repeteix 5 vegades

i = 0
while i < 5:
    print(f'Contador actual: {i}')
    i += 1  # Significa i = i + 1

print("Fin de l'execució")

# Repetim una acció amb un nombre indeterminat de vegades (especialitat de while)

missatge = ""
while missatge != "q":
    missatge = input("Introduiu un missatge (q per a sortir)\n")
    print("El missatge ha estat " + missatge)

