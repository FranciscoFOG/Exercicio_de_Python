# PROGRAMA TESTANDO A MÉDIA (NOTAS) #

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2)/ 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('Com a média {} o aluno está REPROVADO!'.format(media))
elif media >= 5 and media < 7:
    print('Com a média {} o aluno está em RECUPERAÇÂO!'.format(media))
else:
    print('Com a média {} o aluno está APROVADO!'.format(media))