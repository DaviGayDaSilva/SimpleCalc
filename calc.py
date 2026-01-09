import time
import math

print('Olá, você entrou na SimpleCalc, iremos fazer umas perguntas pra calcular! ')
time.sleep(2)
n1 = int(input('Qual é o primeiro numero? '))
print('Vendo Resposta')
time.sleep(2)
n2 = int(input('Qual é o segundo numero? '))
print('Vendo Resposta')
time.sleep(2)

s = n1 + n2
st = n1 - n2
x = n1 * n2
d = n1 / n2
p = n1 ** n2
md = n1 % n2
ptm = (n1 * n2) / 100
raiz_n1 = math.sqrt(n1)
raiz_n2 = math.sqrt(n2)

print('Calculando...')
time.sleep(2)
print('Calculado')
time.sleep(2)
print(f'O Resultado dos numeros {n1} e {n2} é {s} na parte da soma')
time.sleep(2)
print(f'O Resultado do numeros {n1} e {n2} é {st}')
time.sleep(2)
print(f'O Resultado do numeros {n1} e {n2} é {x} na parte de multiplicação')
time.sleep(2)
print(f'O Resultado dos numeros {n1} e {n2} é {d} na parte da divisão')
time.sleep(2)
print(f'O Resultado do numeros {n1} e {n2} é {p} na parte da potencia')
time.sleep(2)
print(f'A raiz quadrada de {n1} é {raiz_n1}')
time.sleep(2)
print(f'A raiz quadrada de {n2} é {raiz_n2}')
time.sleep(2)
print(f'O Resultado de {n1} e {n2} é {md} na parte de modulo')
print(f'O Resultado de {n1} e {n2} é {ptm} na parte de porcentagem')

print('Obrigado por usar o SimpleCalc, caso você pegou de alguma pessoa, que enviou, o link é:')
print('https://github.com/DaviGayDaSilva/SimpleCalc')
