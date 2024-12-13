def calcular_edats(any_actual, persones):
    print(f"Any actual: {any_actual}\n")
    print(f"{'Nom':<15}{'Data naixement':<20}{'Anys que farà aquest any'}")
    print("-" * 50)
    
    for persona in persones:
        nom, any_naixement = persona
        edat = any_actual - any_naixement
        print(f"{nom:<15}{any_naixement:<20}{edat}")
        
if __name__ == "__main__":
    any_actual = 2024
    persones = [
        ("Pere", 2000),
        ("Maria", 1999),
        ("Anna", 2005),
        ("Joan", 1998)  # Añade aquí el cuarto nombre y año de nacimiento
    ]
    
    calcular_edats(any_actual, persones)
