"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
"""

def getNum():
    return int(input("Introduce un número entero (o -1 para terminar): "))

def sumaDigitos(num):
    suma = 0
    while num > 0:
        num = getNum()    
        digito = num % 10
        suma += digito
        num //= 10
        
    return suma

def cantidadNum(num):
    cantidad = 0
    while num != -1:
        num = getNum()
        par = num % 2
        
        if par == 0:
            cantidad += 1
    return cantidad

def main():
    num = getNum()
    res = sumaDigitos(num)
    print(f"La suma de los dígitos de todos los números es: {res}")

    cantidad = cantidadNum(num)
    print(f"La cantidad de números pares ingresados es {cantidad}.")


if __name__ == "__main__":
    main()