import math

class ecuacion_cuadratica:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def calculo(self):    
        discriminante = pow(self.b,2) - 4 * self.a * self.c
        if discriminante < 0:
            return None
        else:
            x_1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            x_2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return x_1, x_2

    def salida(self):
        soluciones = self.calculo()
        if soluciones is None:
            print('No existen soluciones reales.')
        else:
            x_1, x_2 = soluciones
            print(f'Las soluciones a la ecuacion cuadratica son: {x_1} y {x_2}')

ecuacion_1 = ecuacion_cuadratica(2,3,4)
ecuacion_1.salida()
