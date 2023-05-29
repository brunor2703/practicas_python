from pertenece import pertenece


def superposicion(a, b):
    valor=False
    for x in a:
       valor= pertenece(x, b)

    return valor

list1=["rojo", "azul", "naranja"]
list2=["naranja", "mango", "platano"]
print(superposicion(list1, list2))

