dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos km o carro rodou?'))

valor = (dias * 60) + (km * 0.15)

print('O preço total a ser pago pelo aluguel é de {:.2f}'.format(valor))

