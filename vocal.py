def vocal(letra):
    vocales="aeiou"
    if len(letra)==1:
        if letra in vocales:
            return True 
    return False


print(vocal("a"))
print(vocal("d"))
print(vocal("ae"))