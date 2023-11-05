"""
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""
from ej2_2_14 import getNum

def mayorNum():
    mayor = None
    while True:
        num = getNum()
       
        if num == 0:
            break
        if mayor is None or num > mayor:
            mayor = num 
    return mayor

def main():
    mayor = mayorNum()
    
    print(f"El número mayor de los números anteriores es: {mayor}")

if __name__ == "__main__":
    main()