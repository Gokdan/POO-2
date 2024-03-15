class Main:
    @staticmethod
    def pagos(departamento_1,departamento_2,departamento_3):
        ventas_totales = departamento_1 + departamento_2 + departamento_3
        salario_base_trabajadores = float(input('Ingrese salario base de los trabajadores: '))
        salario_departamento_1 = salario_base_trabajadores 
        salario_departamento_2 = salario_base_trabajadores
        salario_departamento_3 = salario_base_trabajadores
        
        if departamento_1 > ventas_totales * 0.33 :
            salario_departamento_1 = salario_departamento_1 + salario_base_trabajadores * 0.2
        
        if departamento_2 > ventas_totales * 0.33 :
            salario_departamento_2 = salario_departamento_2 + salario_base_trabajadores * 0.2
        
        if departamento_3 > ventas_totales * 0.33:
            salario_departamento_3 = salario_departamento_3 + salario_base_trabajadores * 0.2

        return salario_departamento_1, salario_departamento_2 , salario_departamento_3
        
    @staticmethod
    def info():
        departamento_1 = float(input('Ingrese las ventas del departamento 1: '))
        departamento_2 = float(input('Ingrese las ventas del departamento 2: '))
        departamento_3 = float(input('Ingrese las ventas del departamento 3: '))
        salario_departamento_1, salario_departamento_2, salario_departamento_3 = Main.pagos(departamento_1,departamento_2,departamento_3)
        print(f'El salario final en el departamento 1 será ${salario_departamento_1}')
        print(f'El salario base en el departamento 2 será ${salario_departamento_2}')
        print(f'El salario base en el departamento 3 será ${salario_departamento_3}')

Main.info()