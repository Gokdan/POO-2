class Main:
    @staticmethod
    def pago_trabajador(horas_trabajadas,valor_hora):
        if horas_trabajadas <= 40:
            pago = horas_trabajadas * valor_hora
        if 41 <= horas_trabajadas <=48:
            pago = (40 * valor_hora) + (horas_trabajadas-40) * ( 2 * valor_hora)
        if horas_trabajadas >= 48:
            pago = (40 * valor_hora) + (8 *(2 * valor_hora)) + (horas_trabajadas - 48) * (3 * valor_hora) 

        return pago
    @staticmethod
    def info():
        nombre = input('Ingrese el nombre del trabajador: ')
        horas_trabajadas = int(input('Ingrese las horas semanales laboradas: '))
        valor_hora = float(input('Ingrese el valor de la hora normal de trabajo: '))
        print(f'El pago de {nombre} es de ${Main.pago_trabajador(horas_trabajadas,valor_hora):.2f}')

Main.info()