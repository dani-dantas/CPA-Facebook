ticket = float(input('\nTicket: R$ '))

cpa = ticket / 2
conjunto = round(ticket) // 2

if conjunto % 2 != 0: conjunto -= 1

print('CPA (máximo): ' + f'R$ {cpa}')
print('Por conjunto: ' + f'R$ {conjunto}')
