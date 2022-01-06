velocidade = float(input('Digite a velocidade do carro:'))

multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Velocidade permitida siga em frente')
else:
    print('Alerta, voce ultrapassou a velocidade permitida que é de 80 km/h e foi multado!!!')
    print('Sua multa é de {:.2f} R$'.format(multa))