n= int(input("digite um numero para fatoração: "))
f = 1
r = 1
if n == 0:
    print (1)
else:
    fc = True
    while fc:
        r = r*f
        f = f + 1
        if n < f:
            fc = False
            print (r)
    
