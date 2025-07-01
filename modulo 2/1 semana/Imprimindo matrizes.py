def imprime_matriz (minha_matriz):
    x= len (minha_matriz)
    y = len(minha_matriz[0])
    for i in range (x ):
        for j in range (y):
            if j == y-1 :
                num = (minha_matriz[i][j])
                print (num , end = "")
            else:
                num = (minha_matriz[i][j])
                print (num ,"",end = "")
        print ("")
