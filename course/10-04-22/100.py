#-------------------------------------------------
#--------------  Algoritmo 100 -------------------
#-------------------------------------------------

n = int(input("Informe um número com 4 algarismos: "))

a = n / 100

if a % 4 == 0:
  print("O número é multiplo de 4")
else:
  print("O número não é multiplo de 4")
