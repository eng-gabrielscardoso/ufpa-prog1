#-------------------------------------------------
#--------------  Algoritmo 97  -------------------
#-------------------------------------------------

n = int(input("Informe um número: "))

if n % 10 == 0:
  print("É múltiplo de 10")
elif n % 2 == 0:
  print("É múltiplo de 2")
elif n % 5 == 0:
  print("É múltiplo de 5")
else:
  print("Não é múltiplo de 2 nem de 5")
