import random

print('\nSorteio entre 4 alunos para saber a ordem de apresentação do trabalho')

n1 = str(input('Digite o nome do 1° aluno:'))
n2 = str(input('Digite o nome do 2° aluno:'))
n3 = str(input('Digite o nome do 3° aluno:'))
n4 = str(input('Digite o nome do 4° aluno:'))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem de apresentação sera: {}'.format(lista))

##print(lista)



