def fatorial (n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat
condicao = True
while condicao:
    n= int(input("digite um numero para fatoração: "))
    fatorial (n)
    print (fatorial(n))
    if n== -1:
        condicao =False

