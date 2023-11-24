"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

def getPassword():
    return input("Introduce la contraseña: ")

def pruebaPassword(password):
    passOrig = "contraseña"
    if password.replace(" ", "").lower() == passOrig:
        return True
    else:
        return False

def main():
    intentos = 3
    while intentos > 0:
        password = getPassword()
        if pruebaPassword(password):
            print("Has acertado la contraseña!")
            break 
        else:
            print(f"Contraseña incorrecta. Te quedan {intentos - 1} intentos.")
            intentos -= 1
    else:
        print("Agotaste tus intentos. Contraseña bloqueada.")

if __name__ == "__main__":
    main()