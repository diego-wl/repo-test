def es_par(num):
    return num % 2 == 0

num = int(input('Ingrese numero:'))

while (num<=0):
    print('El numero ingresado debe ser mayor a cero')
    num = int(input('Ingrese numero:'))

if es_par(num):
    print('El numero ingresado es par')
else:
    print('El numero ingresado no es par')