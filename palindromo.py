def palindormo(x):
    if x== x[::-1]:
        return True
    else:
        return False
    

palabra=palindormo("amor roma")
print(palabra)
