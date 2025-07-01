def maior_primo(x):
    caraleo = 1
    while caraleo == 1:
        divisor = 1
        primo = 1
        while x / divisor != 1:
            divisor = divisor + 1
            if x % divisor == 0:
                primo = primo + 1
        if primo == 2:      
            return x
            caraleo = 2
        else:
            caraleo = 1
            x = x - 1


            
 


        
