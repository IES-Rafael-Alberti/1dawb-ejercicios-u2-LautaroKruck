"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

def tabla():
    serie = ""
    cont = 1 
    while cont <= 10:
        res = 10 * cont
        serie += f"\n 10 * {cont} = {res} \n"
        cont += 1
    return serie

def main():
    serie = tabla()
    print(serie)

if __name__ == "__main__":
    main()