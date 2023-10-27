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