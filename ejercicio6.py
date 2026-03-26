while True:
    try:
        n = int(input("Cuantos numeros vas a ingresar? "))
        if n > 1:
            break
        else:
            print("Debe ingresar al menos 2 numeros")
    except ValueError:
        print("Ingrese un numero valido")

numeros = []

for i in range(n):
    while True:
        try:
            num = float(input(f"Ingrese numero {i + 1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Ingrese un numero valido")

print("Parejas:")

for i in range(len(numeros)):
    for j in range(len(numeros)):
        if i != j:
            print(f"({int(numeros[i])}, {int(numeros[j])})")
