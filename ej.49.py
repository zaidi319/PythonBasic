import random

# Funció per generar una llista de 20 elements aleatoris
def llista_20_elements():
    llista = [random.randint(1, 100) for _ in range(20)]
    return llista

# Funció per comprovar si hi ha duplicats en una llista (definida anteriorment)
def hi_ha_duplicats(llista):
    elements_vistos = set()
    for element in llista:
        if element in elements_vistos:
            return True
        elements_vistos.add(element)
    return False

# Generar la llista de 20 elements i comprovar si hi ha duplicats
llista_generada = llista_20_elements()
print("Llista generada:", llista_generada)

if hi_ha_duplicats(llista_generada):
    print("La llista generada té elements duplicats.")
else:
    print("La llista generada no té elements duplicats.")
