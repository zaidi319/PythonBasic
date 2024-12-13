def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("intruduce un numero: ")
        if a!=".":
            l.append(int(a))
    return l
s=[]
s=[7, 6, 3, 4, 2]
def lledir_llista():
    s=input(" este numero es mas mayor: ")