"""
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
"""
def contar_digitos_pares_impares(numero):
    digitos_pares = 0
    digitos_impares = 0

    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            digitos_pares += 1
        else:
            digitos_impares += 1
        numero //= 10

    return digitos_pares, digitos_impares

def main():
    total_digitos_pares = 0
    total_digitos_impares = 0

    numero = int(input("Ingresa un número entero positivo (ingresa 0 para finalizar): "))

    while numero != 0:
        if numero < 0:
            print("Por favor, ingresa un número entero positivo.")
        else:
            digitos_pares, digitos_impares = contar_digitos_pares_impares(numero)
            total_digitos_pares += digitos_pares
            total_digitos_impares += digitos_impares

            print(f"En el número {numero}: {digitos_pares} dígitos pares y {digitos_impares} dígitos impares.")

        numero = int(input("Ingresa un número entero positivo (ingresa 0 para finalizar): "))

    print(f"\nTotal de dígitos pares leídos: {total_digitos_pares}")
    print(f"Total de dígitos impares leídos: {total_digitos_impares}")

if __name__ == "__main__":
    main()