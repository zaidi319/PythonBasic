#donada una llista que ens retorni que siguin parells
l=[3, 5, 6, 8, 9, 11, 12]

r=[]
for e in l:
    if e%2==0:
        r.append(e)
print(r)


def parell(x):
    if x%2==0:
        return True
    return False
r=list(filter(parell,l))
print(r)






"""l=[1, 2, 3, 4, 7, 10]
r=list(map(lambda x:x**5,l))
print(r)


l = ["manzana", "pera", "frambuesa", "kiwi", "plátano"]
palabra_mas_larga = max(l, key=len)
print(f"La palabra más larga es: {palabra_mas_larga}")

palabras_ordenadas = sorted(l, key=len)
print(f"Palabras ordenadas de menor a mayor: {palabras_ordenadas}")


def suma(llista):
    ls=[]
    for e in llista:
        ls.append(e)
    return ls 


#programa principal
l = [2, 3, 4]
print(l)
s=suma(l)
print("la lista es esta {} y la modificada es esta {} ")



#parametres
# string/cadena de carcters ?? es pasa pero valor o per referencia
def modifica_string(s):
    s="esto cambia"

s="bondia es esto"
print(s)
modifica_string(s)
print(s)

# per valor
def operacio(a, b, c):
    c = a + b
a = 3
b = 4
c = 0
print(c)
operacio(a, b, c)
print(c)


def axllista(l):
    for i in range(len(l)):
        l[i]*=3

#programa principal
llista=[2, 3, 4]
print(llista)
axllista(llista)
print(llista)"""

