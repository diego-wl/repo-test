# Programa que identifica si un numero es par
def es_par(num):
    return num % 2 == 0

def solicitar_numero():
    num = int(input('Ingrese numero:'))

    while (num<=0):
        print('El numero ingresado debe ser mayor a cero')
        num = int(input('Ingrese numero:'))
    return num

def main():
    num = solicitar_numero()
    if es_par(num):
        print('El numero ingresado es par')
    else:
        print('El numero ingresado no es par')

main()
