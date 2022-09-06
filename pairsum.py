def pairSum(myList, sum):
    listTot = []
    for i in range(len(myList)):
        if myList[i] < sum:
            for j in range(i+1, len(myList)):
                if  myList[i] + myList[j] == sum:
                    listTot.append(str(myList[i]) + "+" +str(myList[j]))
    return listTot
    
print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))