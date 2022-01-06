numero = float(input('Digite um numero para saber se é impar ou par:'))
resto = numero % 2
if resto == 0:
    print('O numero {} é par:'.format(numero))
else:
    print('O numero {} é impar'.format(numero))