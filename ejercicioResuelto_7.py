class Main:
    @staticmethod
    def desigualdad():
        A = int(input('Ingrese el primer numero (A): '))
        B = int(input('Ingrese el segundo numero (B): '))
        
        if (A<B):
            print(f'A ({A}) es menor que B ({B})')
        elif (A==B):
            print(f'A ({A}) es igual a B ({B})')
        else:
            print(f'A ({A}) es mayor que B ({B})')

Main.desigualdad()