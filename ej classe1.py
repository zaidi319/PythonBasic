a="hola"
b=input ("Llegir parula: ")
#mostrar caracter a caracter cadena llegida
for e in b:
    print (e)
#longitd paraula
print(len(b))

#comparar-les 
if a == b:
    print("{} i {} son iguals ". format (a, b))
else:
    print("{} i {} son diferents". format(a, b))

#ajuntar- les amb un guio
print(a+"-"+b)

#repetir-la 3 vagadas
print(b*3)

#mirar si la vocal a es dins b(string:
if "a" in b:
    print("a es dins l'string{}"format)
