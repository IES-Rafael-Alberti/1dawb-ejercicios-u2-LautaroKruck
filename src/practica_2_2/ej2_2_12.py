"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

def getFrase():
    return str(input ("Introduce una frase: "))

def getLetra():
    return str(input ("Introduce una letra: "))

def contar_letras(frase, letra):
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

def main():
    frase = getFrase()
    letra = getLetra()
    cantidad = contar_letras(frase, letra)
    print (f"La letra '{letra}' aparece {cantidad} veces en la cadena.")

if __name__ == "__main__":
    main()

