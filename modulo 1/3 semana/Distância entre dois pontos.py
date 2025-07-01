import math
x1= float(input("Digite a coordenada x do primeiro plano cartesiano:"))
y1= float(input("Digite a coordenada y do primeiro plano cartesiano:"))
x2= float(input("Digite a coordenada x do segundo plano cartesiano:"))
y2= float(input("Digite a coordenada y do segundo plano cartesiano:"))

dist= (math.sqrt(((x1-x2)**2) +((y1-y2)**2)))

if dist>=(10):
    print ("longe", dist)
else:
    print ("perto", dist)
