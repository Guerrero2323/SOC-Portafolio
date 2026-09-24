# Fase 0 - Ezequiel Guerrero
# Mi primer analizador de logs - aprendiendo

print("Hola SOC - Iniciando Fase 0")
print("Objetivo: Aprender a leer logs de intentos fallidos")

# Esto es lo que vamos a mejorar en las próximas semanas
with open("auth.log", "r") as archivo:
    lineas = archivo.readlines()
    print(f"Leí {len(lineas)} líneas del log")
