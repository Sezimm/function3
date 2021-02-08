def nechet_rec(n):
    print(n)
    if n == set():
        return 'End'
    else:
        n.pop()
        return nechet_rec(n)
        

a = set(input())
print(nechet_rec(a))