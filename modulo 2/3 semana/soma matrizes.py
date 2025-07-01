
a = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
b = [2, 3, 4, 5],[6, 7, 8, 9],[10, 11, 12, 13],[14, 15, 16, 17],[18, 19, 20, 21]

def main (a,b):
    (num_lin)= len (a)
    (num_col)=len (a[0])
    c = []
    for i in range(num_lin):
        lin = []
        for j in range(num_col):
            soma= a[i][j]*b[i][j]
            lin.append (soma)
        c.append(lin)
        
    print (c)

    
main(a,b)

