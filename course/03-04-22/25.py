#-------------------------------------------------
#--------------  Algoritmo 25  -------------------
#-------------------------------------------------

date = int(input('Digite uma data no formado ddmmaa: '))

day = date / 10000
month = date % 10000 / 100
year = date % 100

print(f'Dia: {int(day)}\nMês: {int(month)}\nAno: {int(year)}')
