#-------------------------------------------------
#--------------  Algoritmo 122  ------------------
#-------------------------------------------------

a = int(input("Informe o lado a: "))
b = int(input("Informe o lado b: "))
c = int(input("Informe o lado c: "))

if a < b + c and b < a + c and c < a + b:
  print("Podem ser os lados de um triângulo")
else:
  print("Não são lados de um triângulo")
