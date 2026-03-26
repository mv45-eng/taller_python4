while True:
    try:
        n = int(input("¿Cuántos números vas a ingresar? "))
        if n <= 0:
            print("Debe ser mayor que 0.")
            continue
        break
    except ValueError:
        print("Error: ingresa un número entero válido.")
numeros = []
for i in range(n):
    while True:
        try:
            num = int(input(f"Ingrese el número {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Error: debes ingresar un número entero válido.")
original = numeros.copy()
for i in range(len(numeros)):
    intercambio = False
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            intercambio = True
    if not intercambio:
        break 
print("Lista original:", original)
print("Lista ordenada:", numeros)
