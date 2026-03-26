numeros = []
for i in range(3):
    while True:
        try:
            num = int(input(f"Ingresa el número {i+1}: "))
            numeros.append(num)
            break  
        except ValueError:
            print("Error: debes ingresar un número entero válido.")
promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)
