def generar_n_caracs(n, caracter):
    resultado=""
    for i in range(n):
        resultado=resultado+caracter
    return resultado
    



resultado=generar_n_caracs(5,"x")
print(resultado)
