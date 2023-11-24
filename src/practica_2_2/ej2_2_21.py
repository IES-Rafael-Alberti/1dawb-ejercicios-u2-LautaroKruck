"""
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
"""
def calcular_total_pagar(ventas):
    total = sum(ventas)
    if total > 1000:
        descuento = total * 0.1
        total -= descuento
    return total

def main():
    ventas = []
    monto = float(input("Ingresa el monto de la compra (ingresa 0 para finalizar): "))

    while monto != 0:
        if monto < 0:
            print("El monto ingresado es negativo. Por favor, ingresa un monto válido.")
        else:
            ventas.append(monto)

        monto = float(input("Ingresa el monto de la compra (ingresa 0 para finalizar): "))

    total_pagar = calcular_total_pagar(ventas)

    print(f"\nTotal a pagar: ${total_pagar:.2f}")

if __name__ == "__main__":
    main()