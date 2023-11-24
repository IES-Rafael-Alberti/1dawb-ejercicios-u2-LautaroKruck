"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

from practica_2_1.ej2_1_5 import getAge

def años(age):
    serie = ""
    cont = 1
    while cont <= age:
        serie += str(cont) + " "
        cont += 1
    return serie

def main():
    age = getAge()
    res = años(age)
    print(res)

if __name__ == "__main__":
    main()