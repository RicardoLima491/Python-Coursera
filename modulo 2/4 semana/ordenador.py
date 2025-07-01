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


        

