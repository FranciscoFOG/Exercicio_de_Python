# PROGRAMA TESTANDO SALÁRIOS #

salario = float(input('Digite o valor do salario R$: '))

if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))

