# PROGRAMA DESCONTO DE PRODUTO #

valor = float(input('Qual o valor do produto? R$ '))
desc = valor - (valor * 5 / 100)
print('O produto que cUstava {} e após os 5% de desconto é{}'.format(valor, desc))
