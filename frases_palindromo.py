from palindromo import palindromo

def palindromo_frases(cadena):
    cadena_modificada = cadena.lower()
    cadena_modificada = cadena_modificada.replace(" ", "")
    cadena_modificada = cadena_modificada.replace(".", "")
    cadena_modificada = cadena_modificada.replace(",", "")
    cadena_modificada = cadena_modificada.replace("?", "")
    cadena_modificada = cadena_modificada.replace("¿", "")
    cadena_modificada = cadena_modificada.replace("á", "a")
    cadena_modificada = cadena_modificada.replace("é", "e")
    cadena_modificada = cadena_modificada.replace("í", "i")                                           
    cadena_modificada = cadena_modificada.replace("ó", "o")                                            
    cadena_modificada = cadena_modificada.replace("ú", "u")

    return palindromo(cadena_modificada)

frase = palindromo_frases("Abusón, acá no suba")
print(frase)