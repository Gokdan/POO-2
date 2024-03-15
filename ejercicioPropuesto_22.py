class Main:
    @staticmethod
    def salario():
        nombre = input('Ingrese el nombre: ')
        valor_hora = float(input('Ingrese el valor de la hora labor: '))
        horas_mes = int(input('Ingrese el número de horas laboradas al mes: '))
        salario_total = valor_hora * horas_mes
        if salario_total > 450000:
            print(f'Nombre: {nombre}', end= '. Salario total: $')
            print(salario_total)
        else: 
            print(f'{nombre}')

Main.salario()