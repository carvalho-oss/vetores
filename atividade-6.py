import os
os.system ('cls')


print('= INSERINDO NÚMEROS DO VETOR =')
vetor_notas = []
QUANTIDADE_NOTAS = 4

for i in  range(QUANTIDADE_NOTAS):
    nota = float(input(F'Digite sua {i+1}º notas: '))
    vetor_notas.append(nota)
media = sum(vetor_notas) / QUANTIDADE_NOTAS

if media >= 7:
    print(f'\n APROVADO, media:  {media}')
elif media <= 5:
    print (f'\n RECUPERAÇÃO, media:  {media}')
elif media <= 5:
    print(f'\n REPROVADO, media: {media}')
else:
    Print('\n OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')

