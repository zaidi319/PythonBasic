p=""
l=[]
while (p!="%"):
    p = input("Introduje una palabra: ")
    if p!="%": 
        s = p.lower()
        p=s[0]=p[0].ipper()
        l.append(s)
print("las palabras son: {}".format(l))
print("ya hemos acabado¡")









"""p=""
l=[]
while (p!="."):
    p = input("Introduje una palabra: ")
    if p!="." and len(p)==4:
        l.append(p)
    if len(l)==4:
        print("las palabras son: {}".format(l))
        p="."
print("ya hemos acabado¡")"""







