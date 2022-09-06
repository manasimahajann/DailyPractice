import numpy as numpy

def rotate(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer -1
        for i in range(first, last):
            # save top ele
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            matrix[i][-layer-1] = top
            print(matrix)
    return matrix
if __name__ == '__main__': 
    matrix = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(matrix)
    print(rotate(matrix))
