
def soma_matrizes(m1, m2):
    xm1 = len (m1)
    ym1 = len (m1[0])
    xm2 = len (m2)
    ym2 = len (m2[0])
    if  xm1 != xm2 or ym1 != ym2:
        soma_matrizes = False
        return False    
    else:
        xm1 = len (m1[0])
        soma=[]
        matrizsomada=[]
        for i in range(0,(xm1-1)):
            x=(m1[i])
            y=(m2[i])
            soma.append(matrizsomada)
            for j in range(0,(xm1)):
                x= (m1[i][j])
                y= (m2[i][j])
                matrizsomada.append(x+y)
            matrizsomada=[]
        if xm1==1:
            soma.append(matrizsomada)
            x= (m1[0][0])
            y= (m2[0][0])
            matrizsomada.append(x+y)
            

    return (soma)
            
         
    
