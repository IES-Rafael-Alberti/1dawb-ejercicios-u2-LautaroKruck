"""
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
"""

def mostrar_menu():
    print("\nMenú:")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Terminar")

def main():

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            print("texto")
        elif opcion == '2':
            print("texto")
        elif opcion == '3':
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 3.")


if __name__ == "__main__":
    main()