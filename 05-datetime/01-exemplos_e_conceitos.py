'''Trabalhando com date, datetime e time'''

import datetime
#from datetime import date

d = datetime.date(2023, 7, 19) #date.(2023, 7, 19)
print(d)

print(20*"--")

print("Hoje:")
print(datetime.date.today())

print(20*"--")

data_hora = datetime.datetime(2023, 7, 10, 10, 30, 20)
print(data_hora)

print(20*"--")

data_hora = datetime.datetime.now()
print(data_hora)

print(20*"--")

hora = datetime.time(10, 20, 0)
print(hora)
