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
    serie = ""
    cont = 1
    while cont > num :
        serie += str(cont) * "*"
        cont += 1
    return serie


def main():
    num = getNum()
    serie = doSerie(num)
    print(serie)

if __name__ == "__main__":
    main()