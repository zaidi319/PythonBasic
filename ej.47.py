def mostrar_parells():
    for i in range(2, 101, 2):
        print(i, end=', ')
    print()

def mostrar_senars():
    for i in range(1, 101, 2):
        print(i, end=', ')
    print()

# Crida a les funcions per mostrar els resultats
print("Números parells fins a 100:")
mostrar_parells()

print("Números senars fins a 100:")
mostrar_senars()
