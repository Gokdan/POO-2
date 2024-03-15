class Main:
    @staticmethod
    def numero_mayor(A,B,C):
        if A>=B and A>=C:
            return A
        elif B>=A and B>=C:
            return B
        else:
            return C
    
    @staticmethod
    def info():
        A = int(input('Ingrese el primer número: '))
        B = int(input('Ingrese el segundo número: '))
        C = int(input('Ingrese el tercer número: '))
        print(f'El mayor de los números ingresados es: {Main.numero_mayor(A,B,C)}')

Main.info()

