"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

Formula para calcular El capital tras un año.
    amount *= 1 + interest / 100
En donde:
    amount: Cantidad a invertir
    interest: Interes porcentual anual 
"""

def getCantidad():
    return int(input ("Introduce la cantidad a invertir: "))

def getInteres():
    return int(input ("Introduce el interés anual: "))

def getAños():
    return int(input ("Introduce el número de años: "))

def cantidadAnual(cantidad, interes):
    cantidad *= 1 + interes / 100
    return cantidad

def capital(cantidad, años):
    capital = cantidad * años
    return capital
def main():
    cantidad = getCantidad()
    interes = getInteres()
    años = getAños()
    cantidad_anual = cantidadAnual(cantidad, interes)
    res = capital(cantidad_anual, años)
    print(f"{res:.2f}")

if __name__ == "__main__":
    main()

