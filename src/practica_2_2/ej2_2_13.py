"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

def getEntrada():
    return input("Introduce algo (o escribe 'salir' para terminar): ")

def eco(frase):
    if frase.lower() == "salir":
        return False
    else:
        print(frase)
        return True

def main():
    while True:
        entrada = getEntrada()
        if not eco(entrada):
            break

if __name__ == "__main__":
    main()