distancia = float(input('Qual a distancia da sua viagem?'))
print('Voce esta preste a começar uma viagem de {:.2f} km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
    print('O valor da viagem ficou {:.2f}:'.format(preço))
else:
    preço = distancia * 0.45
print('O preço da sua passagem sera de {:.2f} R$'.format(preço))
