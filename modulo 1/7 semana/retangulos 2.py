def main():
    lar= int(input("digite a largura: "))
    alt= int(input("digite a altura: "))
    x= lar
    primeira = 1
    if primeira ==1 :
        while x > 0:
            print ("#", end = "")
            x = x - 1
        print ()
        primeira= 2
    if primeira == 2:
        x = lar 
        x = x -2
        y = alt - 2
        while  y >0:
            y=y-1
            espaco = lar -2
            print("#", end="")
            while espaco>0:
                print(" ", end = "")
                espaco= espaco - 1
            print("#")
        x= lar
        while x > 0:
            print ("#", end = "")
            x = x - 1
        print ()
        
    
main()

