"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
"""

from ej2_2_14 import getNum

def sumaNum(num):
    suma = 0

    while True:
        num = getNum()
       
        if num == 0:
            break
        if num > 0:
            suma += num
    return suma
    
def main():
    num = getNum()
    res = sumaNum(num)
    print(f"La suma de los números anteriores es: {res}")

if __name__ == "__main__":
    main()