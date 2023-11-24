"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

"""

from src.practica_2_1.ej2_1_4 import getNum

def main():
    num = getNum()
    serie(num)

if __name__ == "__main__":
    main()