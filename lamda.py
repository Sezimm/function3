a = int(input('Dlina: '))
b = int(input('Shirina: '))
c = int(input('Vysota: '))

d = (lambda a,b,c: f'Объём бассейна: {a*b*c}')(a,b,c)
print(d)