
def fatorar (n):
    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1
    return (fat)
n = int (input("digite o numero de n: "))
k = int (input("digite o numero de k: "))
resultado = 0
resultado = (fatorar (n))// (fatorar(k)* fatorar(n-k))
print (resultado)
