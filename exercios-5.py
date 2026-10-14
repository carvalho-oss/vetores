import os
os.system ('cls')

print('= INSERINDO NÚMEROS DO VETOR =')
vetor_notas = []
QUANTIDADE_NOTAS = 2

for i in  range(QUANTIDADE_NOTAS):
    nota = float(input(F'Digite sua {i+1}º notas: '))
    vetor_notas.append(nota)

# SUM - SOMAR TUDO QUE ESTÁ NO VETOR.
    soma= sum(vetor_notas)
    media = soma / QUANTIDADE_NOTAS

print ('\n= EXIBINDO NÚMEROS DO VETOR =')
for notas, nota in enumerate(vetor_notas,start=1):
    print(f'{notas}°: {nota}')

    print(f'soma: {soma}')
    print(f'média`{media}')