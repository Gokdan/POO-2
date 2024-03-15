import math
pi = math.pi

class circulo:
    def __init__(self,radio):
        self.radio = radio
    def area_circulo(self):                 #Metodo para el area del circulo
        return  (pi * pow(self.radio,2))
    
    def circunferencia(self):               #Metodo para la circunferencia
        return 2 * pi * self.radio
    
class rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area_rectangulo(self):              #Metodo para el area del rectangulo
        return self.base * self.altura
    
    def perimetro_rectangulo(self):         #Metodo para el perimetro del rectangulo
        return (2 * self.base) + (2 * self.altura)
    
class cuadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def area_cuadrado(self):                #Metodo para el area del cuadrado
        return  self.lado * self.lado
    
    def perimetro_cuadrado(self):           #Metodo para el perimetro del cuadrado
        return self.lado * 4

class triangulo_rectangulo:                 
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area_triangulo(self):               #Metodo para el area del triangulo
        return (self.base * self.altura) / 2
    
    def hipotenusa(self):                   #Metodo para calcular la hipotenusa
        argumento = pow(self.base,2) + pow(self.altura,2)
        return math.sqrt(argumento)

    def perimetro_triangulo(self):          #Metodo para hallar el perimetro del triangulo
        return self.base + self.altura + self.hipotenusa()
    
    def tipo_triangulo(self):               #Metodo para determinar el tipo de triangulo
        if self.base == self.altura and self.base == self.hipotenusa():
            return  'equilátero!'
        
        elif self.base != self.altura and self.base != self.hipotenusa():
            return 'Escaleno!'
        
        else:
            return 'isósceles!'

class Main:         #Clase Main y metodo main para crear instancias de las figuras geometricas y probar los metodos definidos sobre ellas
    @staticmethod
    def main():
        # Instancias de las figuras geométricas
        circulo_1 = circulo(5)  
        rectangulo_1 = rectangulo(4, 6)  
        cuadrado_1 = cuadrado(3)  
        triangulo_rectangulo_1 = triangulo_rectangulo(3, 4)  
        
        print("Área del círculo:", circulo_1.area_circulo(), 'cm cuadrados')
        print("Perímetro del círculo:", circulo_1.circunferencia(), 'cm')
        
        print("Área del rectángulo:", rectangulo_1.area_rectangulo(), 'cm cuadrados')
        print("Perímetro del rectángulo:", rectangulo_1.perimetro_rectangulo(), 'cm')
        
        print("Área del cuadrado:", cuadrado_1.area_cuadrado(), 'cm cuadrados')
        print("Perímetro del cuadrado:", cuadrado_1.perimetro_cuadrado(), 'cm')
        
        print("Área del triángulo rectángulo:", triangulo_rectangulo_1.area_triangulo(), 'cm cuadrados')
        print("Perímetro del triángulo rectángulo:", triangulo_rectangulo_1.perimetro_triangulo(), 'cm')
        
        print("Hipotenusa del triángulo rectángulo:", triangulo_rectangulo_1.hipotenusa(), 'cm')
        print("Tipo de triángulo:", triangulo_rectangulo_1.tipo_triangulo())

Main.main()