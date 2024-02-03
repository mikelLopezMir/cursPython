# Podem modificar el flux d'una aplicació depenent d'una decisió.

age = input("Introduiu la vostra edat:\n")
if age.isnumeric():
    numeric_age = int(age)
    print(f'La vostra edat és {numeric_age}, i en dos anys serà {numeric_age + 2}')
else:
    print("L'edat introduïda no és correcta")

if numeric_age < 18:
    print("Ets menor d'edat.")
elif numeric_age < 30:
    print("Ets jove.")
elif numeric_age < 55:
    print("Ets madur.")
else:
    print("Ets gran. Enhorabona per haver-hi arribat.")