def filtra_palabras_largas(lista, n):
    vacia = []
    for palabra in lista:
        if len(palabra) >= n:
            vacia.append(palabra)
            
    return vacia


lista = ["carro", "bicicleta", "motocicleta"]
n = 20
resultado = filtra_palabras_largas(lista, n)
print(resultado)


