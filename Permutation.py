def permutation(list1, list2):
    if(list1 > list2):
        return False
    list1.sort()
    list2.sort()

    if(list1 == list2):
        return True
    else:
        return False
if __name__ == '__main__': 
    print("permutation")
    print(permutation([8,2,5,9],[8,9  ,2,5]))