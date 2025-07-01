import random
def lista_grande(n):
    lista =[]
    for i in range(n):
        num = (random.randrange(1, 100, 1))
        lista.append(num)
    return (lista)


def ordena(lista):
    fim = (len(lista))
    for i in range(fim-1):
        posição_inicio = i
        for j in range(i+1,fim):
            if lista[j]<lista[posição_inicio]:
               posição_inicio = j
        lista[i],lista[posição_inicio]=lista[posição_inicio],lista[i]
    return(lista)
