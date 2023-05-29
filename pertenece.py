def pertenece(x, a):
    
    for elemnto in a:
        if x== elemnto:
            return True
        
    return False


if __name__ == "__main__":

    x= "uva"
    a= ["manzana", "mango", "uva"]

    respuesta = pertenece(x, a)
    print (respuesta)

    x= 9
    a= [1,6,2,9,11,13]

    respuesta = pertenece(x, a)
    print (respuesta)

    x= 2
    a= [1,6,7,9,11,12]

    respuesta = pertenece(x, a)
    print (respuesta)