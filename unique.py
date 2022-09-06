

def is_unique(listV):
    if(len(listV) > len(set(listV))):
        return False
    else: 
        return True
def is_uniquee(listV):
    newList = []
    for val in listV:
        if val in newList:
            print(val)
            return False
        if val not in newList:
            newList.append(val) 
    return True


if __name__ == '__main__': 
    print("unique")
    print(is_unique([8,2,5,9,9]))
    print(is_uniquee([8,2,5,9,9]))