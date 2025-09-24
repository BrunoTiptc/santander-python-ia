# Crie uma lista dos quadrados dos primeiros n numeros naturais.
def quadrados(n):
    return [i**2 for i in range(1, n+1)]
print(quadrados(10))

