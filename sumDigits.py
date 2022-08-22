def sumOfDigits(n):
    assert n>=0 and int(n) == n, "must be a positive int only"   
    if n == 0:
        return 0
    else:
        return (n%10)+ sumOfDigits(n//10)



if __name__ == "__main__":
    print(sumOfDigits(111))
