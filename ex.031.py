# PROGRAMA DISTÂNCIA X PREÇO #

distancia = float(input('Digite a distancia da viagem: '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem sera de R${:.2f}'.format(preço))
