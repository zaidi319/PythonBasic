#ex 7
def llegir_llista():
    l=[]
    p=""
    while p!=".":
        p=input("intduje un elemento a la lista: ")
        if p!=".":
            l.append(int(p))
    return l

#programa principal
llista = llegir_llista()
r=[]
for i,e in enumerate(llista):
    if llista[i]==e:
        r.append(e)

print("la lista no comapitible cn el elemnto")