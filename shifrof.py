def log_pass(func):
    a = input("Login: ")
    b = input("Password: ")
    func(a,b)

@log_pass
def shifr(a,b):
    print('Login shifr: ', end = '')
    for x in a:
        print(ord(x), end = " " )
    print()
    print('Password shifr: ', end = '')
    for i in b:
        print(ord(i), end = ' ')
    print()

