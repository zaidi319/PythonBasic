def es_primer(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primers_fins_100():
    primers = []
    for num in range(1, 101):
        if es_primer(num):
            primers.append(num)
    return primers

# Obtenir la llista de números primers i comptar-los
primers = numeros_primers_fins_100()
quantitat = len(primers)

# Imprimir els resultats
print("Números primers entre 1 i 100:", primers)
print("Quantitat de números primers entre 1 i 100:", quantitat)
