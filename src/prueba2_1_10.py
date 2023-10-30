"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.

Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

def pedirPizza():

    pizza = ""

    while pizza != "Y" and pizza != "N":
        pizza = input("Quiere una pizza vegetariana (Y/N): ").upper()

    return pizza

def asignarPizza(pizza):

    if (pizza == "Y" ) or (pizza == "N" ):
        res
        return True
    else:
        return False
    
def Ingredientes(pizza):
    if asignarPizza(pizza) == True:
        print
    else:
        print
        return


def main():
    print("\n\n Bienvenido a la pizzería Bella Napoli. \n\n")
    pizza = pedirPizza()

    print(f"Su pizza es ")

if __name__ == "__main__":
    main()

