class Main:
    @staticmethod
    def compra(valor_compra):
        bolita = input('¿El color de la bolita es blanca, verde, amarilla, azul o roja? ')
        if bolita == 'blanca':
            return  valor_compra
        elif bolita == 'verde':
            return valor_compra - (valor_compra * 0.1)
        elif bolita == 'amarilla':
            return valor_compra - (valor_compra * 0.25)
        elif bolita == 'azul':
            return  valor_compra - (valor_compra * 0.5)
        else:
            return valor_compra * 0

    @staticmethod        
    def info():
        valor_compra = float(input('¿Cual es el valor total de su compra? '))
        print(f'Usted debe pagar ${Main.compra(valor_compra):.2f} :)')
Main.info()
