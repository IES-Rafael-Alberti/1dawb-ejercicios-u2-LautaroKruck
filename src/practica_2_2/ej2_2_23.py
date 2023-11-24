"""
Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
"""

def contar_digitos_en_titulo(titulo):
    total_digitos = sum(c.isdigit() for c in titulo)
    return total_digitos

def contar_digitos_en_linea(linea):
    total_digitos = sum(contar_digitos_en_titulo(titulo) for titulo in linea)
    return total_digitos

def procesar_linea(linea, lineas_completas):
    if lineas_completas > 0:
        print(f"Línea completa. Aparecen {contar_digitos_en_linea(linea)} dígitos numéricos.")
    else:
        print("No hay libros en esta línea.")

def main():
    lineas_completas = 0
    linea = []

    titulo = input("Libro: ")

    while titulo != '*':
        if titulo == '/':
            procesar_linea(linea, lineas_completas)

            lineas_completas += 1
            linea = []
        else:
            linea.append(titulo)

        titulo = input("Libro: ")

    print(f"Fin. Se leyeron {lineas_completas} líneas completas.")

if __name__ == "__main__":
    main()