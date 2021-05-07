# PROGRAMA APROVAR EMPRÉSTIMO #

casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do salario: R$ '))
anos = int(input('Diga em quantas parcelas quer pagar: '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')





