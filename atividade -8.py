import os
os.system ('cls')

print('= INSERINDO NÚMEROS DO VETOR =')
vetor_numero = []
QUANTIDADE_NUMEROS = 5

for i in  range(QUANTIDADE_NUMEROS):
    nota = float(input(F'Digite seu {i+1}º numero: '))
    vetor_numero.append(nota)

menor_nota = min(vetor_numero)
maior_nota = max(vetor_numero)

print('\n= EXIBINDO A MENOR E MAIOR NOTAS DO VETOR =')
print(f'Menor numero: {menor_nota}')
print(f'Maior_numero: {maior_nota}')