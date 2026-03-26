while True:
    try:
        n = int(input("Ingrese un numero: "))
        if n > 0:
            break
        else:
            print("Debe ser un número positivo")
    except ValueError:
        print("Ingrese un número válido")

contador = 0

while n > 1:
    nuevo = n // 2
    print(f"{n} / 2 = {nuevo}")
    n = nuevo
    contador += 1

print(f"Se dividio {contador} veces")
