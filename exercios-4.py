import os
os.system ('cls')

print('= INSERINDO NÚMEROS DO VETOR =')
vetor_notas = []
for i in  range(3):
    nota = float(input(F'Digite sua {i+1}º notas: '))
    vetor_notas.append(nota)

print ('\n= EXIBINDO NÚMEROS DO VETOR =')
for notas, nota in enumerate(vetor_notas,start=1):
    print(f'{notas}°: {nota}')