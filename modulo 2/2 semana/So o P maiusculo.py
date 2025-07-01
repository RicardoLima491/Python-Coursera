def maiusculas(frase):
    pmaius=""
    for i in frase:
        x= i
        if x ==("p"):
            y = (i)
            y= y.upper()
            pmaius = pmaius +(y)
        else:
           pmaius = pmaius +(i)

    print(pmaius)
