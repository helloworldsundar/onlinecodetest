#!bin/python3

import sys

"""
get the primary diagonal elements
input : matrix of any size nxn
output : [a,b,...,c] where a,b..c forms the primary diagonal
         of the matrix.
"""
def getPrimaryDiagonal(input_matrix):
    diag = []
    for i in range(len(input_matrix[0])):
        diag.append(input_matrix[i][i])
    return diag
"""
get the secondary diagonal elements
input : matrix of any size nxn
output : [a,b,...,c] where a,b..c forms the secondary diagonal
         of the matrix.
"""
def getSecondaryDiagonal(input_matrix):
    diag=[]
    n=len(input_matrix[0])
    for i in range(n):
        diag.append(input_matrix[n-i-1][i])
    return diag
"""
    input : integer list
    output : sum of elements in integer list
"""
def getSum(intlist):
    sum=0
    for x in intlist:
        sum=sum+x
    return sum
"""
    abs_val(x) - returns non negative result
    if x = -y , return y | else return x
"""
def abs_val (x):
    if (x<0):
        return (-x)
    else:
        return (x)


def main():
    n = int(input().strip())
    arr=[]
    for i in range(n):
        temp = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(temp)
    result = getSum(getPrimaryDiagonal(arr)) - getSum(getSecondaryDiagonal(arr))
    print (abs(result))

main()









