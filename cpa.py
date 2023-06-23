import math

ticket = float(input('\nTicket: R$ '))

cpa = ticket / 2
conjunto = math.ceil(cpa)

print('CPA (máximo): ' + f'R$ {cpa}')
print('Por conjunto: ' + f'R$ {conjunto}')
