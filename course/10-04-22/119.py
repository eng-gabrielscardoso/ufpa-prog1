#-------------------------------------------------
#--------------  Algoritmo 119  ------------------
#-------------------------------------------------

elements = []

MAX = 3

for i in range(MAX):
  n = int(input("Informe um elemento: "))
  elements.append(n)

elements.sort(reverse=True)
print("Ordem crescente: ", elements)
