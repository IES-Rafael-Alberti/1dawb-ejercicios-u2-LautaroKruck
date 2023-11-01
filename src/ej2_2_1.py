"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

def getWord():
    return str(input ("Introduce una palabra: "))

def wordx10(word):
    word = (word + " " )* 10
    return word

def main():
    word = getWord()
    res = wordx10(word)
    print(res)

if __name__ == "__main__":
    main()