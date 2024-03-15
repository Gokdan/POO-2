class Main:
    @staticmethod
    def mayor_peso(A,B,C):
        if A>=B and A>=C:
            return A , 'A'
        elif B>=A and B>=C:
            return B , 'B'
        else:
            return C , 'C'    
    @staticmethod
    def info():
        A = float(input('Ingrese el peso de la esfera A: '))
        B = float(input('Ingrese el peso de la esfera B: '))
        C = float(input('Ingrese el peso de la esfera C: '))
        peso_mayor , identificacion = Main.mayor_peso(A,B,C)
        print(f'La esfera de mayor peso es {identificacion}, con un peso de {peso_mayor} unidades de masa')

Main.info()