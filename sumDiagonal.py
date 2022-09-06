def sumDiagonal(myList2D):
    print("addition")
    n = len(myList2D)
    sum = 0
    for i in range(n):
        sum += myList2D[i][i]
    return sum

myList2D = [[1,2,3],[4,5,6],[7,8,9]] 
 
print(sumDiagonal(myList2D)) # 15