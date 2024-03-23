def pesquisa(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None
l = [10,20,25,30]
print(pesquisa(l,25))
print(pesquisa(l,27))
print(pesquisa(l,30))