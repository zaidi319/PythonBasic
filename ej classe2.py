p=[]
a="1"
while a!=".":
    a = input("introdueixi un element: ")
    if a != ".":
        p.append(int(a))
    else:
        print("Adeu¡")
lp = len(p)
print(range(lp))
print("la llista {} te una longitud {}".format(p,lp))
suma = 0
for e in range(0,lp):
    suma = suma + p[e]
print("La llista {} te una longitud {} i la suma del sues elements es {}".format(p,lp, suma))





"""l=[]
for i in range(4):
    l.append(int(input("Introdueix un numero: ")))
print(l)
suma = 0
for e in l:
    suma = suma + e
print("la suma de tota la llista {} es {}".format(l, suma))
"""