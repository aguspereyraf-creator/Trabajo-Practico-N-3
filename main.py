# main.py

from logica_mision import *

if __name__ == "__main__":

    # Configurar nave (argumentos por nombre en distinto orden)
    configurar_nave(estado="En misión", nombre="Odisea", modelo="Carga")

    print("\n--- Coordenadas actuales ---")
    
    # Obtener coordenadas con unpacking
    x, y, z = obtener_coordenadas()
    print(f"X: {x}")
    print(f"Y: {y}")
    print(f"Z: {z}")

    print("\n--- Registro de tripulación ---")
    
    # Probar *args
    registrar_tripulantes("Ana", "Luis", "Carlos", "Sofía")

    print("\n--- Cálculo de combustible ---")

    combustible = calcular_combustible(1000, 0.5)
print(f"Combustible necesario: {combustible}")
    