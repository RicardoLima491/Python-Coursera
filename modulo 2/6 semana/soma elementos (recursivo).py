lista=[ 258, 338, 351, 378, 386, 439, 454, 505, 523, 534, 567, 616, 633, 694, 737, 823, 973, 976, 980]
def soma_lista(lista):
        tam= len(lista)-1
        if tam==0:
                return lista[0]
        else:
                x=lista[0]
                y=lista[1]
                soma= x+y
                lista.append(soma)
                lista.remove(x)
                lista.remove(y)
        return soma_lista(lista)


def somafor(lista):
        x=0
        for i in (lista):
                x=x+i
        return x
