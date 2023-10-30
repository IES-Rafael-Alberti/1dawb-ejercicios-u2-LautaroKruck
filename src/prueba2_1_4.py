"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

def getNum():
    """
    Solicita un numero por consola.

    Retorna
    -------
    int     
        el un numero introducido
    """
    return int(input ("Introduce un numero: "))

def pruebaNum(num):
    num = num % 2
    if num == 0:
        return True
    else:
        return False

def main():
    num = getNum()
    
    if pruebaNum(num):
        print(f"El numero {num} es par. ")
    else:
        print(f"El numero {num} es impar. ")

if __name__ == "__main__":
    main()