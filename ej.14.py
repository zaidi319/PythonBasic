# Funció que retorna el major de dos números
def gran(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Els dos números són iguals"

# Proves de la funció amb diferents exemples
print(gran(10, 20))  # Ha de retornar 20
print(gran(50, 30))  # Ha de retornar 50
print(gran(5, 5))    # Ha de retornar "Els dos números són iguals"
print(gran(-10, 0))  # Ha de retornar 0
print(gran(3, -5))   # Ha de retornar 3
