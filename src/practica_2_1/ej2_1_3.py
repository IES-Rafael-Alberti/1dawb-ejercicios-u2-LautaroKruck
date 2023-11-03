"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""

def getNum1():
    """
    Solicita un numero por consola.

    Retorna
    -------
    int     
        el numero introducido
    """
    return int(input ("Introduce un numero: "))

def getNum2():
    """
    Solicita otro numero por consola.

    Retorna
    -------
    int     
        el otro numero introducido
    """
    return int(input ("Introduce otro numero: "))

def pruebaDivision(num1 , num2):
    
    if num2 == 0:
        return True
    else:
        return False

def main():
    num1 = getNum1()
    num2 = getNum2()
    if pruebaDivision(num1, num2):
        print("Error, no se puede dividir entre cero. ")
    else:
        print(f"El resultado es {num1 // num2}")

if __name__ == "__main__":
    main()