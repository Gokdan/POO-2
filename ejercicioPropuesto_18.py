'''
Se tiene la siguiente información de un empleado: 
 · código del empleado, 
 · nombres, 
 · número de horas trabajadas al mes, 
 · valor hora trabajada, 
 · porcentaje de retención en la fuente
 Haga un algoritmo que muestre: código, nombres, salario bruto y salario neto. 
'''

class Empleado:
    def __init__(self,codigo,nombre,horasTrabajadas,valorHora,porcentajeRetencion):
        self.codigo = codigo
        self.nombre = nombre
        self.horasTrabajadas = horasTrabajadas
        self.valorHora = valorHora
        self.porcentajeRetencion = porcentajeRetencion

    def salarioBruto(self):
        return (self.horasTrabajadas) * (self.valorHora)
    
    def salarioNeto(self):
        return (self.salarioBruto()) - (self.salarioBruto()*self.porcentajeRetencion)
    
empleado_1 = Empleado(7,'Daniel',8,14000,0.09)
print(f'El codigo del empleado es: {empleado_1.codigo}')
print(f'El nombre del empleado es: {empleado_1.nombre}')
print(f'El salario bruto del empleado es: ${empleado_1.salarioBruto()}')
print(f'El salario neto del empleado es: ${empleado_1.salarioNeto()}')

