from prueba2_1_4 import getNum

def pruebaNum(num):
    return num > 0

def serieNum(num):
    serie = ""
    cont = 1
    while cont <= num:
        serie += str(cont) + ", "
        cont += 2
    return serie

def main():
    num = getNum()
    if pruebaNum(num):
        res = serieNum(num)
        if res:
            print(res)
        else:
            print("No hay números impares en el rango.")
    else:
        print("Debe ingresar un número entero positivo.")

if __name__ == "__main__":
    main()