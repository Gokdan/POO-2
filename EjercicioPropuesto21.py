from math import sqrt
class Main:
    
    @staticmethod
    def perimetro(lado1,lado2,lado3):
        return lado1 + lado2 + lado3
    
    @staticmethod
    def semiperimetro(lado1,lado2,lado3):
        return Main.perimetro(lado1,lado2,lado3)/2
    
    @staticmethod
    def area(lado1,lado2,lado3):
        s = (Main.semiperimetro(lado1,lado2,lado3))      #Semiperimetro
        return sqrt((s * (s - lado1) * (s - lado2) * (s - lado3)))  #Formula de Herón
    

    @staticmethod
    def info():
        lado1 = float((input('Ingrese la longitud del primer lado del triangulo: ')))
        lado2 = float((input('Ingrese la longitud del segundo lado del triangulo: ')))
        lado3 = float((input('Ingrese la longitud del tercer lado del triangulo: ')))

        print(f'Perimetro del triangulo: {Main.perimetro(lado1,lado2,lado3):.2f} unidades')
        print(f'Semiperimetro del triangulo: {Main.semiperimetro(lado1,lado2,lado3):.2f} unidades')
        print(f'Area del triangulo: {Main.area(lado1,lado2,lado3):.2f} unidades cuadradas')

Main.info()