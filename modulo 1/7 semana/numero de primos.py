def n_primos(n):
    x=0
    y=2
    primo = 0
    somaprimo=0
    while x!=n:
        x=x+1
        y=1
        primo = 1
        while y!=n:
            y=y+1
            if x%y==0:
                primo = primo +1

        if primo==2:
            somaprimo= somaprimo+1
    return somaprimo
            
            
            


