def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix un nom: ")
        if a != ".":
            l.append(a)
    return l

def noms_que_comencen_per(l, c):
    m = []
    for e in l:
        senar = len(e) % 2 == 1
        if senar:
            aux = len(e) // 2
            if e[aux].lower() == c.lower():
                m.append(e)
        else:
            aux = len(e) // 2 - 1
            if e[aux].lower() == c.lower() or e[aux + 1].lower() == c.lower():
                m.append(e)
    print(f"Els elements de la llista {l} que contenen '{c}' són: {m}")

# Programa principal
l = llegir_llista()
c = input("Introdueix un caràcter: ")
noms_que_comencen_per(l, c)
