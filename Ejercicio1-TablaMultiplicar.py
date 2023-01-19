def tabla(equis):
    for x in range(1, 11):
        res = equis * x
        print("{} x {} = {}".format(equis, x, res))

valor=int(input("Dame el valor para imprimir la tabla"))
tabla(valor)