x = int (input("Digite um número inteiro: "))
divisor = 1
primo = 1
if x <= 1:
    print ("não primo")
else:
    while x / divisor != 1:
        divisor = divisor + 1
        if x % divisor == 0:
            primo = primo + 1
if primo == 2:      
    print ("primo")
else:
    print ("não primo")
        
        
    
    