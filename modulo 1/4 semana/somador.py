n= int(input('digite o numero a ser somado: '))
a=2
total= 0
while a>0 or n>0:
		a=n % 10
		n=n//10
		total = (total + a)
print ('O total é',total)