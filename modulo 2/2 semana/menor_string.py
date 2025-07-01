def menor_string(meu_string):
    x=meu_string[0]
    x=x.capitalize()
    x=x.strip()
    for i in meu_string:
        y = i
        y=y.capitalize()
        y=y.strip()
        if x > y:
            x = y
    return x
        
        
