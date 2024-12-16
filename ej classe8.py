a = int(input("Escribe un numero: "))
b = int(input("escribe un numero: "))
c = int(input("escribe un numero: "))
if a > b:
    if b > c:
        print("{} es myor que {} y esto es mayor que {}".format(a, b, c))
    elif b<c:
        if a>c:
            print("{} es mayor que {} y esto es mayor que {}".format(a, b, c))
        elif c>a:
            print("{} es mayor que {} y esto es mayor que {}".format(c, a, b))
        