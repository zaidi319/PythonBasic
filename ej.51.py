def crear_llista_fitxer(l):
    llista = []
    try:
        with open(l, 'r') as fitxer:
            for línia in fitxer:
                paraules = línia.split()
                llista.extend(paraules)
    except FileNotFoundError:
        print(f"El fitxer {l} no s'ha trobat.")
    return llista
# Prova de la funció amb un fitxer d'exemple
l = 'exemple.txt'
llista_paraules = crear_llista_fitxer(l)
print("Llista de paraules:", llista_paraules)

