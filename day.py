a = int(input('Skolko dney proshlo s NG: '))
b = input('Vysokosny li god?(y/n): ')
if b == 'n':
    print("Do NG ostalos': ", 365-a)
else:
    print("Do NG ostalos': ", 366-a)