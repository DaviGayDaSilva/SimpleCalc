import time
import math
import random

print('Olá, você entrou na SimpleCalc, iremos fazer umas perguntas pra calcular! ')
time.sleep(1)

# Entradas
n1 = int(input('Qual é o primeiro número? '))
print('Vendo resposta...')
time.sleep(1)
n2 = int(input('Qual é o segundo número? '))
print('Vendo resposta...')
time.sleep(1)

# Operações básicas
s = n1 + n2
st = n1 - n2
x = n1 * n2
p = n1 ** n2
ptm = (n1 * n2) / 100
raiz_n1 = math.sqrt(n1)
raiz_n2 = math.sqrt(n2)
media = (n1 + n2) / 2
mdc = math.gcd(n1, n2)
mmc = (n1 * n2) // math.gcd(n1, n2) if n1 != 0 and n2 != 0 else 0
raiz_cubica_n1 = n1 ** (1/3)
raiz_cubica_n2 = n2 ** (1/3)

# Proteção de divisão por zero
if n2 != 0:
    d = n1 / n2
    di = n1 // n2
    md = n1 % n2
else:
    d = di = md = 'Ops! Divisão por zero não é permitida.'

# Fatorial com proteção de negativos
f_n1 = math.factorial(n1) if n1 >= 0 else 'Não existe fatorial de número negativo'
f_n2 = math.factorial(n2) if n2 >= 0 else 'Não existe fatorial de número negativo'

# Número aleatório entre os dois
ale = random.randint(min(n1, n2), max(n1, n2))

print('Calculando...')
time.sleep(1)
print('Calculado')
time.sleep(1)

# Impressão dos resultados
print(f'\nSoma: {s}')
print(f'Subtração: {st}')
print(f'Multiplicação: {x}')
print(f'Divisão: {d}')
print(f'Divisão inteira: {di}')
print(f'Módulo: {md}')
print(f'Potência: {p}')
print(f'Porcentagem (n1*n2/100): {ptm}')
print(f'Raiz quadrada de {n1}: {raiz_n1}')
print(f'Raiz quadrada de {n2}: {raiz_n2}')
print(f'Fatorial de {n1}: {f_n1}')
print(f'Fatorial de {n2}: {f_n2}')
print(f'Número aleatório entre {n1} e {n2}: {ale}')
print(f'Valor absoluto de {n1}: {abs(n1)}')
print(f'Valor absoluto de {n2}: {abs(n2)}')
print(f'Média: {media}')
print(f'{n1} é {"par" if n1 % 2 == 0 else "ímpar"}')
print(f'{n2} é {"par" if n2 % 2 == 0 else "ímpar"}')
print(f'MDC: {mdc}')
print(f'MMC: {mmc}')
print(f'Raiz cúbica de {n1}: {raiz_cubica_n1}')
print(f'Raiz cúbica de {n2}: {raiz_cubica_n2}')

# Tabelas de multiplicação
print(f'\nTabuada de {n1}:')
for i in range(1, 11):
    print(f'{n1} x {i} = {n1*i}')

print(f'\nTabuada de {n2}:')
for i in range(1, 11):
    print(f'{n2} x {i} = {n2*i}')

print('\nObrigado por usar o SimpleCalc! Confira o link original:')
print('https://github.com/DaviGayDaSilva/SimpleCalc')
