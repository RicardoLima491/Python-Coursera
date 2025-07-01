import Triangulo_retangulo


def test():
        import Triângulos_semelhantes
        t1= Triângulos_semelhantes.Triangulo(2,3,4)
        t2= Triângulos_semelhantes.Triangulo(5,6,8)
        a= t1.perimetro()
        b= t2.perimetro()

        
        
        if a%b == 0 or b%a == 0:
                return True
        else:
                return False
        return a,b
    
def test1():
        import Triângulos_semelhantes
        t2= Triângulos_semelhantes.Triangulo(4,6,8)
        a= t2.perimetro()

        return a
    

    
test()
test1()
