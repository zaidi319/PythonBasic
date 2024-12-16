def mostra_menu():
    print("""
        Menú del programa principal:
          1. Calculadora de números sencers: suma
          2. Calculadora de números sencers: resta
          3. Calculadora de números sencers: multiplicació
          4. Calculadora de números sencers: divisió entera
          5. Calculadora de números sencers: reste de la divisió entera
          6. Calculadora de números sencers: potència
          7. Calculadora de números reals: suma
          8. Calculadora de números reals: resta
          9. Calculadora de números reals: multiplicació
          10. Calculadora de números reals: divisió real
          11. Calculadora de números reals: potència
          12. Sortir
    """)
    op = input("Elegeixi una opció del menú: ")
    return op
def suma_numeros_enters():
    print("Estic sumant números enters \n")
    a = int(input("Introdueixi el primer número: "))
    b = int(input("Introdueixi el segon número: "))
    print("La suma de {} més {} és {}".format(a, b, a+b))

def resta_numeros_enters():
    print("Estic restant números enters \n")
    a = int(input("Introdueixi el primer número: "))
    b = int(input("Introdueixi el segon número: "))
    print("La resta de {} menys {} és {}".format(a, b, a-b))   


#Programa principal
op = mostra_menu()
match(op):
    case "1":
        suma_numeros_enters()
    case "2":
        resta_numeros_enters()
    case "3":
        multiplicacio_numeros_enters()
    case "4":
        divisio_entera_numeros_enters()
    case "5":
        modul_numeros_enters()
    case "6":
        potencia_numeros_enters()
    case "7":
        suma_numeros_reals()
    case "8":
        resta_numeros_reals()
    case "9":
        multiplicacio_numeros_reals()
    case "10":
        divisio_numeros_reals()
    case "11":
        potencia_numeros_reals()
    case "12":
        print("Sortir!!")
    case _:
        print("Opció no vàlida!!")



