ledef cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            valor= int(input("digite o valorde cada coluna["+ str(i)+"]["+ str(j)+"]"))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def le_matriz():
    lin= int(input("digite o numero de linhas da matriz: "))
    col= int(input("digite o numero de colunas da matriz: "))
    tab= 0
    matriz= cria_matriz(lin,col)
    while tab < lin:
        print (matriz[tab])
        tab= tab+ 1
        
    
le_matriz()
