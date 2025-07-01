class ordenador:
    def ordem(self,lista):
        fim = (len(lista))
        for i in range(fim-1):
            posição_inicio = i
            for j in range(i+1,fim):
               if lista[j]<lista[posição_inicio]:
                   posição_inicio = j
            lista[i],lista[posição_inicio]=lista[posição_inicio],lista[i]
        return(lista)
    def remove_repetidos(self,lista):
        x = []
        for i in lista:
            if i not in x:
                x.append(i)
        x.sort()
        lista=x
        return (lista)
    def cria_lista(self):
        tamanho=int(input("Número de itens na lista:"))
        num = int(input("Qual objeto na lista:"))
        lista =[]
        lista.append(num)
        for i in range(tamanho):
            num = num+3 
            lista.append(num)
            x = num//4
            lista.append(x)
        return (lista)


        
import random
def lista_grande(n):
    lista =[]
    for i in range(n):
        num = (random.randrange(1, 1000, 1))
        lista.append(num)
    return (lista)


def ordem(lista):
    fim = (len(lista))
    for i in range(fim-1):
        posição_inicio = i
        for j in range(i+1,fim):
            if lista[j]<lista[posição_inicio]:
               posição_inicio = j
        lista[i],lista[posição_inicio]=lista[posição_inicio],lista[i]
    return(lista)

def busca(lista,x):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro<= ultimo:
        meio =(primeiro + ultimo)//2
        if x ==lista[meio]:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio-1
                print (meio)
            else:
                primeiro = meio+1
                print(meio)
    return False
