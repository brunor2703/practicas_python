def traducir(palabra):
    palabra_sueco=""
    for letra in palabra:
        if letra not in ["a","e","i","o","u"," "]:
            palabra_sueco=palabra_sueco+letra+"o"+letra
        else:
            palabra_sueco=palabra_sueco+letra
    return palabra_sueco


traduccion=traducir("esto es divertido")
print(traduccion)



