real = float(input('Digite um valor em reais (R$):'))
##dolar = float(input('Entre com a cotação atual do dolar(US):'))

dolar = real / 5.22

print('Voce pode comprar U$ {:.2f} dolares usando o valor de R$ {:.2f} reais'.format(real, dolar))
