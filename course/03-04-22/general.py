#-------------------------------------------------
#--------------  Algoritmo 23  -------------------
#-------------------------------------------------

a = int(input('Imprima um número de três casas: '))

d = int(a % 100 / 10)

print(f'Algarismo da casa das dezenas: {int(d)}')

#-------------------------------------------------
#--------------  Algoritmo 25  -------------------
#-------------------------------------------------

date = int(input('Digite uma data no formado ddmmaa: '))

day = date / 10000
month = date % 10000 / 100
year = date % 100

print(f'Dia: {int(day)}\nMês: {int(month)}\nAno: {int(year)}')

#-------------------------------------------------
#--------------  Algoritmo 34  -------------------
#-------------------------------------------------

n = int(input('Entre com um número: '))

ant = n - 1
suc = n + 1

print(f'O antecessor de {n} é {ant}, e o sucessor é {suc}')

#-------------------------------------------------
#--------------  Algoritmo 38  -------------------
#-------------------------------------------------

n = float(input('Entre com um número com ponto: '))

print('A terça parte é ', n / 3)

#-------------------------------------------------
#--------------  Algoritmo 39  -------------------
#-------------------------------------------------

a = float(input('Informe a nota 1: '))
b = float(input('Informe a nota 2: '))

media = (a + b) / 2

print('A média é ', media)

#-------------------------------------------------
#--------------  Algoritmo 40  -------------------
#-------------------------------------------------

dividendo = float(input('Informe o dividendo: '))
divisor = float(input('Informe o divisor: '))

quoc = dividendo / divisor
rest = dividendo % divisor

print('Dividendo: ', dividendo)
print('Divisor: ', divisor)
print('Quociente: ', quoc)
print('Resto: ', rest)

#-------------------------------------------------
#--------------  Algoritmo 41  -------------------
#-------------------------------------------------

a = float(input('Informe um número a: '))
b = float(input('Informe um número b: '))
c = float(input('Informe um número c: '))
d = float(input('Informe um número d: '))

mp = (a * 1 + b * 2 + c * 3 + d * 4) /10

print('A média ponderada é ', mp)

#-------------------------------------------------
#--------------  Algoritmo 42  -------------------
#-------------------------------------------------

import math

ang = float(input('Informe o ángulo em graus: '))

PI = 3.14159

rang = (ang * PI) / 180

print('Seno: ', math.sin(rang))
print('Cosseno: ', math.cos(rang))
print('Tangente: ', math.tan(rang))
print('Cossecante: ', 1 / math.sin(rang))
print('Secante: ', 1 / math.cos(rang))
print('Cotangente: ', 1 / math.tan(rang))

#-------------------------------------------------
#--------------  Algoritmo 43  -------------------
#-------------------------------------------------

import math

n = float(input('Informe um numero: '))

log = math.log(n) / math.log(10)

print(f'Logaritmo: {log}')

#-------------------------------------------------
#--------------  Algoritmo 44  -------------------
#-------------------------------------------------

import math 

logaritmando = float(input('Entre com o logaritmando: '))
base = float(input('Entre com a base: '))

logaritmo = math.log(logaritmando) / math.log(base)

print(f'O logaritmo de {logaritmando} na base {base} é {logaritmo}')
