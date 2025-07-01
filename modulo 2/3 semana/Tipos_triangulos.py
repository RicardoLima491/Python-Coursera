class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimetro(self):
        if self.a >= 1 and self.b >=1 and self.c >= 1:
            p = self.a + self.b + self.c
        return p
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return("equilátero")
        elif self.a == self.b or self.c == self.b or self.a == self.c:
            return ("isósceles")
        else:
            return ("escaleno")

    def retangulo(self):
        if (self.a * self.a) == ((self.b * self.b)+(self.c * self.c)):
            return True
        elif (self.b * self.b) == ((self.a * self.a)+(self.c * self.c)):
            return True
        elif (self.c * self.c) == ((self.b * self.b)+(self.a * self.a)):
            return True
        else:
            return False
 
