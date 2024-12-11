import random
import time

# Funció on expliquem què passa
def intro():
    print("En una època on els gegants governen Menorca. Nosaltres necessitem menjar,\n"
          "Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.\n"
          "Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran\n"
          "i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.\n")

# Funció on demanem a quin talaiot volem anar
def canvi_talaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(talaiot_elegit):
    print("T'estas apropant al talaiot...")
    time.sleep(2)
    print("Està fosc i és tenebrós...")
    time.sleep(2)
    print("Un gran gegant salta davant teu, t'agafa i ...\n\n")
    time.sleep(2)
    
    gegantamic = random.randint(1, 2)
    if talaiot_elegit == str(gegantamic):
        print("Et convida a menjar...\n")
        return True
    else:
        print("Se't menja d'un mos...ÑAMÑAMÑAM\n")
        return False

# Funció principal
def main():
    partida_nova = "si"
    punts = 0
    while partida_nova == "s" or partida_nova == "si":
        intro()
        talaiot_elegit = canvi_talaiot()
        if trobada(talaiot_elegit):
            punts += 10
        else:
            print(f"Has perdut! Punts totals aconseguits: {punts}\n")
            break
        partida_nova = input("Vols tornar a jugar (mejar)? Introdueixi si o no: ")
        print("\n")
    if partida_nova != "s" and partida_nova != "si":
        print(f"Punts totals aconseguits: {punts}\n")

if __name__ == "__main__":
    main()
