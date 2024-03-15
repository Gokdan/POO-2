class Main:
    def __init__(self,numero_inscripcion,nombre,apellido,patrimonio,estrato_social):
        self.numero = numero_inscripcion
        self.nombre = nombre
        self.apellido = apellido
        self.patrimonio = patrimonio
        self.estrato = estrato_social
    
    def valor_matricula(self):
        valor_inicial = 50000
        if (self.patrimonio >= 2000000) and (self.estrato > 3) :
            return valor_inicial + self.patrimonio * 0.03
        else: 
            return valor_inicial
    
    def info(self):
        print(f'El estudiante con número de inscripcion {self.numero} y nombre {self.nombre} {self.apellido} debe pagar ${self.valor_matricula()}')

estudiante_1 = Main(12,'Pepe','Perez',3000000,4)
estudiante_1.info()


