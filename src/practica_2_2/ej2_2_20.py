"""
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
"""
def pedir_frase():
    return input("Ingresa una frase: ")

def buscar_coincidencia(frase, letra):
    posicion_coincidencia = None

    for i, caracter in enumerate(frase):
        if caracter == letra:
            posicion_coincidencia = i

        else:
            print(f"No hay coincidencia en la posición {i}")

    return posicion_coincidencia

def main():

    frase = pedir_frase()
    letra = input("Ingresa una letra: ")

    posicion_coincidencia = buscar_coincidencia(frase, letra)

    if posicion_coincidencia is not None:
        print(f"Se encontró una coincidencia en la posición {posicion_coincidencia}")
    else:
        print(f"No se encontró la letra en la frase")

if __name__ == "__main__":
    main()