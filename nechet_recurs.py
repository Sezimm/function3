def nechet_rec(n):
    if n == 0:
        return 'End'
    else:
        if n%2==1:\
            print(n)
        return nechet_rec(n-1)

n = int(input('Do kakogo chisla? '))
print(nechet_rec(n))

    
        

