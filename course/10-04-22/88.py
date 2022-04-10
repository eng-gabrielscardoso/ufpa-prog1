#-------------------------------------------------
#--------------  Algoritmo 88  -------------------
#-------------------------------------------------

from time import sleep

C = True

while (C):
  print("*" * 13)
  print("*CALCULADORA*")
  print("*" * 13)
  print("+ para somar")
  print("- para subtrair")
  print("* para multiplicar")
  print("/ para dividir")
  
  _operation = str(input("Informe a operação: "))

  if _operation == "" or len(_operation) <= 0:
    print("CAMPOS VAZIOS NÃO SÃO PERMITIDOS")
    sleep(2)
    continue

  _operator = float(input("Digite o operando: "))
  _operand = float(input("Digite o operando: "))

  _calc = f"{_operator} {_operation} {_operand}"

  _result = 0

  if _operation == "+":
    _result = _operator + _operand
  elif _operation == "-":
    _result = _operator - _operand
  elif _operation == "*":
    _result = _operator * _operand
  elif _operation == "/":
    _result = _operator / _operand
  else:
    print("OPERAÇÃO NÃO PÔDE SER REALIZADA")
    sleep(2)
    continue

  print(f"O resultado de {_calc} = {_result}")

  new = int(input("Deseja fazer uma nova operação (1 - Sim; 0 - Não): "))

  if new == 1:
    print("Iniciando nova operação...")
    sleep(2)
    continue
  else:
    print("Encerrando calculadora...")
    sleep(2)
    break
