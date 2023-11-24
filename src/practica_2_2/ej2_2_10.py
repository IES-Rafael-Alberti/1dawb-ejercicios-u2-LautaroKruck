"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

from src.practica_2_1.ej2_1_4 import getNum


def comprobarNum(num):
    if num <= 1:
        return False 
        
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False 
        else:
            return True 

def main():
    num = getNum()

    if comprobarNum(num) == True:
        print(f"El número {num} es primo")
    else: 
        print(f"El número {num} no es primo")

if __name__ == "__main__":
    main()

