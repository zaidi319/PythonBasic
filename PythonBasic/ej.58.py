def imprimir_patron():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()  # Afegeix una nova línia després de cada fila

# Crida a la funció per mostrar el patró
imprimir_patron()
