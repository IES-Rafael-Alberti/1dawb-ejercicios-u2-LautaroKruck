"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
from practica_2_1.ej2_1_4 import getNum
from ej2_2_3 import pruebaNum

def serieNum(num):
    serie = ""
    cont = num
    while cont > 0 :
        serie += str(cont) + ", "
        cont -= 1
    serie = serie + "0"
    return serie

def main():
    num = getNum()
    if pruebaNum(num):
        res = serieNum(num)
        print(res)
    else:
        print("Debe ingresar un número entero positivo.")

if __name__ == "__main__":
    main()