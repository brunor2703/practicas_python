def max_de_tres(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
    

print(max_de_tres(16,9,5))
print(max_de_tres(9,17,6))
print(max_de_tres(5,9,19))
print(max_de_tres(18,9,18))
