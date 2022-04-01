#-------------------------------------------------
#--------------  Algoritmo 44  -------------------
#-------------------------------------------------

import math 

logaritmando = float(input('Entre com o logaritmando: '))
base = float(input('Entre com a base: '))

logaritmo = math.log(logaritmando) / math.log(base)

print(f'O logaritmo de {logaritmando} na base {base} é {logaritmo}')
