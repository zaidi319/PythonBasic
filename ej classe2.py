p=[]
a="1"
while a!=".":
    a = input("introdueixi un element: ")
    if a != ".":
        p.append(int(a))
    else:
        print("Adeu¡")
print("la llista {} te una longitud {}".format(p,len(p)))

"""l={}
for i in range(4):
    l.append(int(input("Introdueix un numero: ")))
print(l)
suma = 0
for e in l:
    suma = suma + e
print("la suma de tota la llista {} es {}".format(l, suma))
"""