
def removeDuplicates(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist

print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))