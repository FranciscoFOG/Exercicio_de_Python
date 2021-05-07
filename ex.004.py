# PROGRAMA ANALISANDO OBJETOS #

a = input('Digite  algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('So tem espaços ?', a.isspace())
print('E um numero ?', a.isnumeric())
print('E alfabetico ?', a.isalpha())
print('E alfanumerico ?', a.isalnum())
print('Esta em maiúsculas ?', a.isupper())
print('Esta em minúsculas ?', a.islower())
print('Esta capitalizada ?', a.istitle())
