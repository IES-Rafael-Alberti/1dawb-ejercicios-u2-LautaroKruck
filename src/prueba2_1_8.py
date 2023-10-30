"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	        Puntuación

Inaceptable	    0.0
Aceptable	    0.4
Meritorio	    0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""

def getPuntuacion():
    """
    Solicita la puntuación por consola.
    
    Retorna
    -------
    float     
        una cadena de numeros con la puntuación introducida
    """
    return float(input ("Introduce la puntuación (0.0 / 0.4 / 0.6 o más): "))

def comprobarPuntuacion(puntos):
    
    if puntos == 0.0 or puntos == 0.4 or puntos >= 0.6:
        return True
    else:
        return False

def pruebaPuntuacion(puntos):
    if puntos == 0.0:
        return "Inaceptable"
    elif puntos == 0.4:
        return "Aceptable"
    elif puntos >= 0.6:
        return "Meritorio"

def Dinero(puntos):
    dinero = puntos * 2400
    return dinero

def main():
    puntos = getPuntuacion()
    if comprobarPuntuacion(puntos) == True:
        nivel = pruebaPuntuacion(puntos)
        dinero = Dinero(puntos)
        print(f"Su nivel es {nivel}, recibirá {dinero:.0f} €.")
    else:
        print("Error, introduzca una puntuacion posible. ")

if __name__ == "__main__":
    main()




