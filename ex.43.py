# PROGRAMA TESTAR IMC #

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura **2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso ideal atenção!!!.')
elif 18.5 <= imc < 25:
    print('Parabéns você esta no peso ideal.')
elif 25 <= imc < 30:
    print('Você esta com sobrepeso atenção!!!.')
elif 30 <= imc < 40:
    print('Você está com obesidade cuidado!!!.')
elif imc >= 40:
    print('Você esta com obesidade mórbida Pegigo!!!.')