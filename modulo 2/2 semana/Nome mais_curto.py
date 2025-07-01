lista=[" raul "," paula","josé","ab      ","ana "]
def mais_curto(lista):
    x= lista[0]
    x=x.strip().capitalize()
    for i in lista:
        y= i
        y=y.strip().capitalize()
        if len (x) > len(y):
            x= y                    

    print (x)

mais_curto(lista)
