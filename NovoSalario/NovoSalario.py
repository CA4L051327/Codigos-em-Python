alario = float(input('Digite o salario do funcionario: R$'))

novo = salario + (salario * 15 / 100)

print("O funcionario que ganhava R${:.3f} com 15% de aumento passa a receber R${:.3f}".format(salario, novo))

