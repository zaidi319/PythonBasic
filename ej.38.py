"""
Escriure un programa que demani dues paraules i ens digui si rimen o no. Rimen quan coincideixen les 
3 darreres lletres i rimen un poc quan coincideixen les 2 darreres, si no ens ha de dir que no rimen.
"""

x=input("")
y=input("")
if x[-3:]==y[-3:]:
    print("{} i {} rimen perquè les 3 últimes lletres són iguals".format(x,y))
    