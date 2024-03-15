from math import sqrt
class Main:
    @staticmethod
    def perimetroTriangulo(lado):
        return lado*3
    
    @staticmethod
    def alturaTriangulo(lado):
        return (sqrt(3)*lado)/2
    

    @staticmethod
    def areaTriangulo(lado):
        return sqrt(3)*pow(lado,2)/4   
    @staticmethod
    def info():
        lado = float((input('Ingrese la longitud del lado del triangulo equilatero: ')))
        print(f'El perimetro del triangulo equilatero es: {Main.perimetroTriangulo(lado):.2f} unidades')
        print(f'La altura del triangulo es: {Main.alturaTriangulo(lado):.2f} unidades')
        print(f'El area del triangulo es: {Main.areaTriangulo(lado):.2f} unidades cuadradas')

Main.info()