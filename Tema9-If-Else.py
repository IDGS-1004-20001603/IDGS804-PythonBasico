print("Sumar dos numeros")
num1 = input('Dame el primer numero: ')
num2 = input('Dame el segundo numero: ')
res = int(num1) + int(num2)

print("La suma de {0} + {1} es: {2}".format(num1, num2, res))

if (num1 > num2):
    print("El numero {0} es mas grande que {1}".format(num1, num2))
else:
    print("El numero {0} es mas pequeño que {1}".format(num1, num2))

print("----Nuevo Programa-----")
edad = int(input("Ingresa tu edad: "))

if (edad > 18):
    print("Eres mayor de edad")
elif (edad == 18):
    print("Tienes 10 añoss!!!")
else:
    print("No eres mayor de edad")


'''
AND
OR
NOT
>, <, >=, <=, !
'''
valor1 = 200
valor2 = 2
valor3 = 1000

if (valor1 > 1000 and valor2 > 2) or valor3 < 2000:
    print("Resultado")
