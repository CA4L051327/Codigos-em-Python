print('-' * 15)

medida = float(input('Digite uma distancia em metros:'))

centimetros = medida * 100
milimetros = medida * 1000

print('A media de {} corresponde a {:.0f} e {:.0f}'.format(medida, centimetros, milimetros))