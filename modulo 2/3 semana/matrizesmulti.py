
a=[[1,2,3],[4,5,6]]
b=[[1,2],[3,4],[5,6]]

def mat_mul(a,b):
    num_linhas_a, num_colunas_a = len(a),len(a[0])
    num_linhas_b, num_colunas_b = len(b),len(b[0])
    assert num_colunas_a == num_linhas_b
    c=[]
    for linha in range(num_linhas_a):
        c.append([])
        for coluna in range(num_colunas_b):
            c[linha].append(0)
            for i in range(num_colunas_a):
                c[linha][coluna]+=a[linha][i]*b[i][coluna]
    print( c)


mat_mul(a,b)
