"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
"""

from ej2_2_14 import getNum

def sumaDigitos(num):
    suma = 0
    while num > 0:
        digito = num % 10
        suma += digito
        num //= 10
    return suma

def cantidadNum():
    cantidad = 0
    while True:
        num = getNum()
       
        if num == -1:
            break
        par = num % 2
        if par == 0:
            cantidad += 1
    return mayor

def main():
    num = getNum()
    
    if num < 0:
        print("El número ingresado no es positivo.")
    else:
        res = sumaDigitos(num)
        print(f"La suma de los dígitos del número es: {res}")

if __name__ == "__main__":
    main()