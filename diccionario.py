def traduccion(frase):
    diccionario = {"merry":"god","christmas":"julio","and":"och","happy":"gott","new":"nytt","year":"ar"}
    lista = frase.split()
    lista_sueco = []
    for palabra in lista:
        if diccionario[palabra.lower()]:
            lista_sueco.append(diccionario[palabra.lower()])
    return lista_sueco



texto = traduccion('Merry Christmas and Happy new year')
print(texto)



    



