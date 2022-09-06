
def powerOf(num, exp):
    assert num>=0 and int(num) == num, "must be a positive int only"   

    if exp == 0:
        return 1
    if exp == 1:
        return num

    return num * powerOf(num, exp-1)

if __name__ == "__main__":
    print(powerOf(2,-4))