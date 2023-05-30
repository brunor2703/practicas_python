def palabras_numeros(lista):
    lista_vacia=[]

    for palabra in lista:
        lista_vacia.append(len(palabra))
    return lista_vacia
resultado=palabras_numeros(["", "azul","hola","         r"])
print(resultado) 
