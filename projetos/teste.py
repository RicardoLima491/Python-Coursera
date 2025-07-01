def incomodam(x):        
                print ('incomodam ',end="")
                
def  elefantes(n):
        x=1
        if x==1:
                x='Um'
                print( x,'elefante incomoda muita gente')
                x=2
        if x<=n:
                print(x,'elefantes ',end='')
                y=x
                while y>0:
                        incomodam(x)
                        y=y-1
                print('muito mais')
                x=x+1
                return elefantes(n-2)
                
        
                
                
