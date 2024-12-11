def gran_de_tres(a,b,c):
    if a>b:
        if b>c:
            print("{} es mayor que {} que es mayor que {}".format(a,b,c))
        elif b==c:
            print("{} es mayor que {} que es igual que {}".format(a,b,c))
        else:
            if a>c:
                print("{} es mayor que {} que es mayor que {}".format(a,b,c))
            elif c>a:
                print("{} es mayor que {} que es mayor que {}".format(a,b,c))
            else:
                print("{} i {} son iguales y mayores que {}".format(a,b,c))
    elif b>a:
        if a>c:
            print("{} és major que {} que és major que {}".format(b,a,c))
        elif a==c:
            print("{} és major que {} que és igual que {}".format(b,a,c))
        else:
            if b>c:
                print("{} és major que {} que és major que {}".format(b,c,a))
            elif c>b:
                print("{} és major que {} que és major que {}".format(c,b,a))
            else:
                print("{} i {} són iguals i majors que {}".format(b, c, a))
    else:
        if a>c:
            print("{} i {} són iguals i majors que {}".format(a,b,c))
        elif c>a:
            print("{} és major que {} que és igual que {}".format(c,a,b))
        else:
            print("Tots són iguals i valen {}".format(a))

#Programa principal

gran_de_tres(1,1,1)
gran_de_tres(1,2,3)
gran_de_tres(3,2,1)
gran_de_tres(2,3,1)
gran_de_tres(2,1,3)
gran_de_tres(2, 2, 3)
gran_de_tres(1, 2, 2)
gran_de_tres(1, 3, 1)