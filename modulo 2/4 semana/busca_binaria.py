lista1=[]
def busca(lista,x):
    primeiro = 0
    ultimo = len(lista)-1
    lista1=[]
    while primeiro<= ultimo:
        meio =(primeiro + ultimo)//2
        if x ==lista[meio]:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio-1
                lista1.append (meio)                
            else:
                primeiro = meio+1
                lista1.append (meio)
    for i in (lista1):
        print (i)
    return False 

