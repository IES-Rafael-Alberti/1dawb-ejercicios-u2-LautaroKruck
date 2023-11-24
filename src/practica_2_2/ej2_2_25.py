"""
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""

def obtener_palabra_mas_larga(frase):
    palabras = frase.split()
    if not palabras:
        return None

    return max(palabras, key=len)

def main():
    frase = input("Ingresa una frase: ")

    palabra_mas_larga = obtener_palabra_mas_larga(frase)

    if palabra_mas_larga is not None:
        cantidad_palabras = len(frase.split())
        print(f"\nLa palabra más larga es: '{palabra_mas_larga}'")
        print(f"Había {cantidad_palabras} palabra(s) en la frase.")
    else:
        print("La frase está vacía.")

if __name__ == "__main__":
    main()