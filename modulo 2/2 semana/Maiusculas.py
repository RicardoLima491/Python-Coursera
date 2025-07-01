frase='Ricardo E LindoPrOgRaMaMoS em python!Página inicialEm andamentoConcluído'
def maiusculas(frase):
    pmaius=""
    for i in frase:
        x= i
        if x.isupper():
            y = (i)
            y= y.upper().strip()
            pmaius = pmaius +(y)


    return(pmaius)
