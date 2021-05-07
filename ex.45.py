# JOGO JOKENPÔ #

from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('CPU jogou {}'.format(itens[cpu]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if cpu == 0: # cpu jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('CPU VENCE')
    else:
        print('JOGADA INVÁLIDA !!!')

elif cpu == 1: # cpu jogou PAPEL
    if jogador == 0:
        print('CPU VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA !!!')

elif cpu == 2: # cpu jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('CPU VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÀLIDA !!!')

