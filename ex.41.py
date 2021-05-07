# PROGRAMA CLASSIFICANDO ATLETAS #

from datetime import date
atual = date.today().year

nascimento = int(input('Digite ano nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria é Mirim.')
elif idade <= 14:
    print('Sua categoria é Infantil.')
elif idade <= 19:
    print('Sua categoria é Junior.')
elif idade <= 25:
    print('Sua categoria é Sênior.')
else:
    print('Sua categoria é Master.')