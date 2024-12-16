# Funció per imprimir números de l'1 al 10 en ordre invers
def imprimir_invers():
    for i in range(10, 0, -1):
        print(i, end=' ')
    print()  # Per a saltar a una nova línia després de mostrar els números

# Crida a la funció per mostrar els resultats
imprimir_invers()
