def ordenada(lista):
    fim = (len(lista))
    for i in range(fim-1):
        j = i+1
        if lista[i] > lista[j]:
           return False
    return True
               
    
        

