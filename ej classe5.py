def llegir_llista():
    l=[]
    a="1"
    while a!=".":
        a=input("Introduic una paraula: ")
        if a!=".":
            l.append(a)
        else:
            print("adeu!")
    return l 
#programa principal

l = llegir_llista()
cl = st(l)
if len(l)==len(cl):
    print("No hi ha cap paraula repeida")
else:
    print("No hi ha de repetidas, pero encara no se quines")
    
