def inversa(palabra):
    reverso=""
    for letra in palabra:
        reverso=letra+reverso
    return reverso

prueba=inversa("hola bruno")
print(prueba)



