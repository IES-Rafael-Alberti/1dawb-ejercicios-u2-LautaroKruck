"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""

def pedirNombre():
    """
    Solicita un nombre por consola.

    Retorna
    -------
    str     
        una cadena de caracteres con el nombre introducido
    """
    return input ("Introduce tu nombre: ")

def pedirSexo():
    """
    Solicita el sexo por consola.

    Retorna
    -------
    str     
        un caracter con el tipo de sexo (M/F)
    """

    sexo = ""
    while sexo != "M" and sexo != "F":
        sexo = input("Introduce tu sexo (M/F): ").upper()


    return sexo

def asignarGrupo(nombre , sexo):
    """
    Asigna el grupo del curso según su nombre y sexo.
    
    Parámetros
    ----------
    str     
        el nombre de un alumno
    str     
        el sexo del alumno
    
    Retorna
    ---------
    str     
        un caracter con el tipo de sexo (M/F)
    """

    inicialNombre = nombre[0:1].upper()
    grupo = ""
    if (sexo == "M" and inicialNombre >= "N") or (sexo == "F" and inicialNombre < "M"):
        grupo = "A"
    else:
        grupo = "B"

    return grupo

def main():
    nombre = pedirNombre()

    sexo = pedirSexo()

    print(f"Estás em el grupo {asignarGrupo(nombre, sexo)}")

if __name__ == "__main__":
    main()
