def two_sum(listV, findNum):
    dict_v = {}
    count = 0
    for val in listV:
        if val > findNum:
            continue
        finding = findNum - val
        for newVal in listV:
            if(newVal == finding):
                dict_v[count] = [val, newVal]
                count = count+1
    return dict_v    

def two_summ(listV, target):
    for i in range(len(listV)):
        for j in range(i+1, len(listV)):
            if listV[i] == listV[j]:
                continue
            elif listV[i]+listV[j] == target:
                print(listV[i],listV[j])

if __name__ == "__main__":
    print("two sum")
    print(two_sum([1,2,3,4,5,6, 10], 11))
    two_summ([1,2,3,4,5,6, 10], 11)