#-------------------------------------------------
#--------------  Algoritmo 123  ------------------
#-------------------------------------------------

a = int(input("Informe o lado a: "))
b = int(input("Informe o lado b: "))
c = int(input("Informe o lado c: "))

if a < b + c and b < a + c and c < a + b:
  if a == b and b == c and a == c:
    print("Triângulo equilátero")
  elif a == b or a == c or b == c:
    print("Triângulo isósceles")
  else:
    print("Triângulo escaleno")

else:
  print("Não são lados de um triângulo")