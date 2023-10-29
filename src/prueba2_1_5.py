"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
def getAge():
    """
    Solicita una edad por consola.

    Retorna
    -------
    int     
        una cadena de numeros con la edad introducida
    """
    return int(input ("Introduce tu edad: "))

def getIngreso():
    """
    Solicita el ingreso mensual por consola.

    Retorna
    -------
    int     
        una cadena de numeros con el ingreso mensual introducido
    """
    return int(input ("Introduce tu ingreso mensual: "))

def pruebaAge(age):
    age = age
    if age >= 16:
        return True
    else:
        return False

def pruebaIngreso(ingreso):
    ingreso = ingreso
    if ingreso >= 1000:
        return True
    else:
        return False

def main():
    age = getAge()
    ingreso = getIngreso()
   
    if pruebaAge(age) and pruebaIngreso(ingreso):
        print("Tienes que tributar. ")
    else:
        print("No tienes que tributar. ")

if __name__ == "__main__":
    main()