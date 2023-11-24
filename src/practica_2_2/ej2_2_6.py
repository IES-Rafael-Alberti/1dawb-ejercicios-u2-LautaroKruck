"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""

from src.practica_2_1.ej2_1_4 import getNum


def doSerie(num):
    for i in range(1, num + 1):
        serie = "*" * i
        print(serie)

def main():
    num = getNum()
    doSerie(num)

if __name__ == "__main__":
    main()