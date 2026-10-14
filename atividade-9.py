import os
os.system ('cls')

print('= INSERINDO NÚMEROS DO VETOR =')
numeros = []
pares = 0
ímpares = 0
QUANTIDADE_NOTAS = 6

for i in range(QUANTIDADE_NOTAS):
    nota =  int(input(F'Digite sua  {i+1}º notas: '))
    Vetor_numeros.append(numero)

    # Verificação de par ou ímpar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n--- Resultados ---")
print(f"Números digitados: {numeros}")
print(f"Quantidade de  pares: {pares}")
print(f"Quantidade de ímpares: {ímpares}")
