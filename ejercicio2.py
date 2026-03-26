while True:
    try:
        cantidad = int(input("¿Cuántos números vas a ingresar?: "))
        if cantidad <= 0:
            print("Debes ingresar un número mayor que 0.")
            continue
        break
    except ValueError:
        print("Error: ingresa un número entero válido.")
numeros = []
for i in range(cantidad):
    while True:
        try:
            num = int(input(f"Ingrese el número {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Error: debes ingresar un número entero válido.")
mayor = max(numeros)
menor = min(numeros)
print("El número mayor es:", mayor)
print("El número menor es:", menor)
