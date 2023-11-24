"""
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(numeros):
    return sum(1 for numero in numeros if es_primo(numero))

def ingresar_numeros():
    numeros_ingresados = []
    numero = int(input("Ingresa un número mayor que 1 (ingresa 0 para finalizar): "))

    while numero != 0:
        if numero > 1:
            numeros_ingresados.append(numero)
        else:
            print("Por favor, ingresa un número mayor que 1.")

        numero = int(input("Ingresa un número mayor que 1 (ingresa 0 para finalizar): "))

    return numeros_ingresados

def main():
    numeros_ingresados = ingresar_numeros()
    cantidad_primos = contar_primos(numeros_ingresados)

    print(f"\nSe ingresaron {cantidad_primos} números primos.")

if __name__ == "__main__":
    main()