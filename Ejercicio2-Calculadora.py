import os


class Operaciones:
    def __init__(self):
        pass

    def suma(self, num1, num2):
        res = num1 + num2
        return res

    def resta(self, num1, num2):
        res = num1 - num2
        return res

    def multiplicacion(self, num1, num2):
        res = num1 * num2
        return res

    def division(self, num1, num2):
        try:
            res = num1 / num2
            return res
        except ZeroDivisionError:
            print("El divisor no puede ser 0")


def main():
    os.system('cls')
    ob = Operaciones()
    opcion = -1
    res = 0

    while (opcion != 0):
        print('Menú de opciones \n1.- Suma \n2.- Resta \n3.- Multiplicación \n4.- División \n5.- Salir\n')
        opcion = int(input('Elige una opción del menú: '))

        if (opcion == 5):
            break
        os.system('cls')

        num1 = int(input('Ingresa el primer numero: '))
        num2 = int(input('Ingresa el segundo numero: '))
        if(opcion == 1):
            res = ob.suma(num1, num2)
        elif(opcion == 2):
            res = ob.resta(num1, num2)
        elif(opcion == 3):
            res = ob. multiplicacion(num1, num2)
        elif(opcion == 4):
            res = ob.division(num1, num2)
        
        print('El resultado es: {}'.format(res))

if __name__ == '__main__':
    main()