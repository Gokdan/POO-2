class Main:
    @staticmethod
    def esfera_diferente():
        esfera_A = float(input('Ingrese el peso de la esfera A: '))
        esfera_B = float(input('Ingrese el peso de la esfera B: '))
        esfera_C = float(input('Ingrese el peso de la esfera C: '))
        esfera_D = float(input('Ingrese el peso de la esfera D: '))
        
        if ((esfera_A == esfera_B) and (esfera_A == esfera_C)):
            if esfera_A > esfera_D:
                print ('La esfera D es la difente y es la de menor peso')
            else:
                print('La esfera D es la diferente y es la de mayor peso')
        elif ((esfera_A == esfera_B) and (esfera_A == esfera_D)):
            if esfera_A > esfera_C:
                print('La esfera C es la diferente y es la de menor peso')
            else:
                print('La esfera C es la diferente y es la de mayor peso')

        elif ((esfera_A == esfera_C) and (esfera_A == esfera_D)):
            if esfera_A > esfera_B:
                print('La esfera B es la diferente y es la de menor peso')
            else:
                print('La esfera B es la diferente y es la de mayor peso')
        
        else:
            if esfera_A > esfera_B:
                print('La esfera A es la diferente y es la de mayor peso')
            else:
                print('La esfera A es la diferente y es la de menor peso')

Main.esfera_diferente()

