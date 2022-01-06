import random

print('\nSorteio entre 4 alunos para saber quem irá apagar a lousa')

lista = input('Digite o nome do 1° aluno:'), \
        input('Digite o nome do 2° aluno:'), \
        input('Digite o nome do 3° aluno:'), \
        input('Digite o nome do 4° aluno:'), \

print('\nos alunos a serem sorteados são: ', lista)
print('\no aluno(a) sorteado foi:{}'.format(random.choice(lista)))



