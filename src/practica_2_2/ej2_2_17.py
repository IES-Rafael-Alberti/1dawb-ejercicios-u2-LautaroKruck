"""
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
"""
from ej2_2_14 import getNum

def sumaDigitos(num):
    suma = 0
    while num > 0:
        digito = num % 10
        suma += digito
        num //= 10
    return suma

def main():
    num = getNum()
    
    if num < 0:
        print("El número ingresado no es positivo.")
    else:
        res = sumaDigitos(num)
        print(f"La suma de los dígitos del número es: {res}")

if __name__ == "__main__":
    main()