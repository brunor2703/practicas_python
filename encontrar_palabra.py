def encuentra_palabra_mas_larga(lista):
    palabra_mayor=len(lista[0])
    palabra_mostrar=lista[0]

    for palabra in lista:
        if palabra_mayor<= len(palabra):
            palabra_mostrar= palabra
            palabra_mayor= len(palabra)
        else:
            palabra_mostrar=palabra_mostrar
    return palabra_mostrar

lista=["o", "abcd", "aeiou", "hola_bruno"]
palabra=encuentra_palabra_mas_larga(lista)
print(palabra)

