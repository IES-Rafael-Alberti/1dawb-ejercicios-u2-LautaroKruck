"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""
from ej2_1_1 import getAge

def pruebaAge(age):
    if age < 4:
        return "gratis"
    elif age >= 4 and age < 18:
        return "5€"
    elif age >= 18:
        return "10€"

def main():
    age = getAge()
    entrada = pruebaAge(age)
    print(f"El precio de la entrada es {entrada}")

if __name__ == "__main__":
    main()

