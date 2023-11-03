"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

from ej2_1_1 import getAge

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