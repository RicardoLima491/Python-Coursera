def  é_hipotenusa(x):
    i=1
    j=1
    while j<=x:
        while i<=x:
            i=i+1
            if x**2 == (i**2+j**2):
                return True
        i=1
        j=j+1
        
def soma_hipotenusas(n):
    x= 1
    soma = 0

    while n>=x:
        if  é_hipotenusa(n):
            soma= soma + n
        n=n-1
        
    return soma

            
    
        
