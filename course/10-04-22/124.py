#-------------------------------------------------
#--------------  Algoritmo 124  ------------------
#-------------------------------------------------

a = int(input("Informe o lado a: "))
b = int(input("Informe o lado b: "))
c = int(input("Informe o lado c: "))

major = sides = 0

if a < b + c and b < a + c and c < a + b:
  if a > b and a > c:
    major = a ** 2
    sides = b ** 2 + c ** 2
  else:
    if b > c:
      major = b ** 2
      sides = a ** 2 + c ** 2
    else:
      major = c ** 2
      sides = a ** 2 + b ** 2

  if major == sides:
    print("Triângulo retângulo")
  elif major > sides:
    print("Triângulo obtusangulo")
  elif major < sides:
    print("Triângulo acutangulo")
else:
  print("Não são lados de um triângulo")
