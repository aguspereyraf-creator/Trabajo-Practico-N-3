#1. Función calcular_combustible (Retorno de valor):
def calcular_combustible(distancia, consumo):
    combustible_necesario = distancia * consumo
    return combustible_necesario

#2 Función configurar_nave (Argumentos por Nombre y Default):
def configurar_nave(nombre, modelo="Explorador", estado="Óptimo"):
    print(f"Nave '{nombre}' configurada.")
    print(f"Modelo: {modelo}")
    print(f"Estado: {estado}")

#3. Función obtener_coordenadas (Retorno de Tupla):
def obtener_coordenadas():
    x = 120
    y = -45
    z = 300
    return (x, y, z)

#4.Función registrar_tripulantes (Argumentos Variables *args):
def registrar_tripulantes(*tripulantes):
    print("Tripulantes registrados:")
    for tripulante in tripulantes:
        print(f"- {tripulante}")

