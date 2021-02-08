import random
def rand_100(func):
    a = []
    for x in range(100):
        a.append(random.randint(10,50))
    print(a)
    func(a)

@rand_100
def list_1(a):
    print(set(a))

