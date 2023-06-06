def carac_freq(cadena):
    frecuencia = {}
    for caracter in cadena:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

cadena = "abbabcbdbabdbdbabababcbcbab"
frecuencia = carac_freq(cadena)
print(frecuencia)

