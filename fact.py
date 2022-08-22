def fact(n):
    assert n>=0 and int(n) == n, "must be a positive inr only"  
    if n in [0,1]:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))