# PROGRAMA JOGO ADVINHAR O NÚMERO #

from random import randint
computador = randint(0, 5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta adivinhar
if jogador == computador:
    print('PARABENS!! Você conseguiu vencer! ')
else:
    print('GANHEI!!! Eu pensei no numero {} e não no {}!'.format(computador, jogador))

