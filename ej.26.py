s = input("intruduce paraula: ")
l = list(s)
r=[]
for e in l:
    if e in "AEIOU":
        r.append(".")
    else:
        r.append(e)
s = ".".join(r)
print(s)