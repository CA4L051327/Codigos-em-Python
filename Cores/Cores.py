nome = 'Carlos'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print('Ola muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))