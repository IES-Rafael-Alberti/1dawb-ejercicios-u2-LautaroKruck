"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
"""

def getNum():
    return int(input("Introduce un número entero (o 0 para terminar): "))
    
def main():
    suma = 0

    while True:
        num = getNum()
       
        if num == 0:
            break
        suma += num

    print(f"La suma de los números anteriores es: {suma}")

if __name__ == "__main__":
    main()
