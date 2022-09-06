

def max_prod(listV):
    multiply = 0
    for i in range(len(listV)):
        for j in range(i+1, len(listV)): 
            if multiply < listV[i]*listV[j]:
                multiply = listV[i]*listV[j]


    return multiply

if __name__ == '__main__': 
    print("MaxProd")
    print(max_prod([8,2,5,9]))