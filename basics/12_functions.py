# Si el codi és molt llarg, podem fer petits paquets de codi que es poden reutilitzar. Aquests paquets de codi es diuen funcions.
# Aquests paquets es diuen funcions. Aquestes funcions poden tenir arguments (valors que es passen a la funció) i poden retornar valors.

# Exemple de codi monolític sense funcions

primer_nombre = input("Introdueixi el nombre del qual es calcularà el factorial\n")
primer_nombre = int(primer_nombre)
for i in range(1,primer_nombre):
    primer_nombre *= i
print(f'El factorial és {primer_nombre}')

# Exemple de codi amb funcions
# Generarem la funció factorial
# Com a paràmetre, la funció rebrà un nombre enter
# La funció retornarà el factorial d'aquest nombre, un altre enter

def factorial(n):
    for i in range(1,n):
        n *= i
    return n

primer_nombre = input("Introdueixi el nombre del qual es calcularà el factorial\n")
primer_nombre = int(primer_nombre)
print(f'El factorial és {factorial(primer_nombre)}')
