def max_en_lista(lista):
    mayor=0
    for i in range(len(lista)):
        if i==0:
            mayor=lista[0]
        else:
            if mayor<lista[i]:
                mayor=lista[i]
                
    return mayor
resultado=max_en_lista([18])
print(resultado)