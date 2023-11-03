"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

def getPassword():
    """
    Solicita una contraseña por consola.

    Retorna
    -------
    str     
        una cadena de caracteres con la contraseña introducida
    """
    return input ("Introduce la contraseña: ")

def pruebaPassword(password):
    passOrig = "contraseña"
    if password.replace(" ", "").lower() == passOrig:
        return True
    else:
        return False

def main():
    password = getPassword()
    if pruebaPassword(password):
        print("Has acertado la contraseña! ")
    else:
        print("Siga jugando. ")

if __name__ == "__main__":
    main()