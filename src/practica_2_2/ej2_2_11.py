"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

from ej2_2_1 import getWord

def alReves(word):
    word = word[::-1]
    return word

def main():
    word = getWord()
    res = alReves(word)
    print (res)

if __name__ == "__main__":
    main()  