import math

oposto = float(input('Comprimento cateto oposto:'))
adjacente = float(input("Comprimento catedo adjacente:"))

print('O comprimento da hipotenusa é {:.2f}'.format(math.hypot(oposto, adjacente)))

##hipotenusa = math.hypot(7, 5)

