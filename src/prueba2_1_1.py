"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""

def getName():
    """
    Solicita el nombre por consola.

    Retorna
    -------
    str     
        una cadena de caracteres con el nombre introducido
    """
    return str(input ("Introduce tu nombre: "))

def getAge():
    """
    Solicita una edad por consola.

    Retorna
    -------
    int     
        una cadena de numeros con la edad introducida
    """
    return int(input ("Introduce tu edad: "))

def pruebaAge(age):
    age = age
    if age >= 18:
        return True
    else:
        return False

def main():
    name = getName()
    age = getAge()
    if pruebaAge(age):
        print(f"Hola {name}, eres mayor de edad. ")
    else:
        print(f"Hola {name}, eres menor de edad. ")

if __name__ == "__main__":
    main()