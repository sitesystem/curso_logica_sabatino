# IMPORTAR UNA LIBRERÍA DE FUNCIONES MATEMÁTICAS
import math

# ENTRADAS DE DATOS
número_1 = float(input("Escribe el 1er número: "))
número2 = float(input("Escribe el 2do número: "))

# PROCESOS (Cálculos y/u Operaciones Matemáticas y Lógicas)
suma = número_1 + número2
resta = número_1 - número2
multiplicación = número_1 * número2
división = número_1 / número2
potencia1 = número_1 ** número2
potencia2 = pow(número_1, número2)
cuadrado = número_1 ** 2
cubo = pow(número2, 3)
raíz_cudrada1 = math.sqrt(9)
raíz_cudrada2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

# SALIDA DE DATOS
print("La suma =", round(suma, 2))
print("La suma = " + str(round(suma, 2))) # CONCATENACIÓN (Unión de textos)
# Convertir un tipo de dato en otro tipo de dato (CASTEO)
print(f"La suma = {round(suma, 2)}")

print(f"La potencia 1 = {potencia1}")
print(f"La potencia 2 = {potencia2}")
print(f"El cuadrado de número1 = {cuadrado}")
print(f"El cubo de número 2 = {cubo}")
print(f"La raíz cuadrada 1 = {raíz_cudrada1}")
print(f"La raíz cuadrada 2 = {raíz_cudrada2}")
print(f"La raíz cúbica = {raíz_cúbica}")