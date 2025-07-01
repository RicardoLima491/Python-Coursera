lista=[175, 258, 338, 351, 378, 386, 439, 454, 505, 523, 534, 567, 616, 633, 694, 737, 823, 973, 976, 980]
def encontra_impares(lista):
        if x ==0 :
                return lista
        else:
                x=lista[0]
                lista.remove(x)
                if x %2!=0:                   
                        lista.append(x)
        return encontra_impares(lista)






def impares(lista):
        for i in (lista):
                if i %2==0:
                        lista.remove(i)
        return lista
                
