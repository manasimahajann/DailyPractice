def fact(n):
    assert n>=0
    if n in [0,1]:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))