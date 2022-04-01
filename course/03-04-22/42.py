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
