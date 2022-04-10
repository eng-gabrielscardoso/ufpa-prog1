#-------------------------------------------------
#--------------  Algoritmo 138  ------------------
#-------------------------------------------------

option = int(input("Informe um número de 1 a 12: "))

months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

if option > 12 or option <= 0:
  print("Opção inválida")
else:
  for i, month in enumerate(months):
    if i + 1 == option:
      print("O mês escolhido foi:", month)
