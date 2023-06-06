def correcion(expresion):
    frase = ""
    letra_anterior = ""
    for letra in expresion:
        if letra_anterior == " " and letra != " ":
            frase = frase + letra
            
        if letra_anterior == "." and letra != " ":
            frase = frase + " "
        if letra_anterior != "." and letra_anterior != " ":
            frase = frase + letra

        letra_anterior = letra
    return frase
resultado = correcion("!Esto es muy    divertido.einteresante")
print(resultado)

