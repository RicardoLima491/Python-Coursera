
def menor_nome(lista):
    x= lista[0]
    x=x.strip().capitalize()
    for i in lista:
        y= i
        y=y.strip().capitalize()
        if len (x) > len(y):
            x= y                    

    return (x)


