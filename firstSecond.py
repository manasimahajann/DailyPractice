def firstSecond(givenList):
    # givenList.sort()
    # print(givenList) 
    # newSet = set(givenList)
    # print(list(newSet)[-1],list(newSet)[-2])
     
    a = givenList   #make a copy 
    a.sort(reverse=True) 
    print(a)
 
    first = a[0]
 
    second = None
 
    for element in givenList:
 
        if element != first:
 
            second = element
 
            return first, second

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
firstSecond(myList)
