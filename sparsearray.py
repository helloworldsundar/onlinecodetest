#!bin/python3

def findInstanceCount (arr,element):
    sum = 0
    for ( t in arr) :
        if (t == element):
            sum += 1
    return sum


def main():
    n = int(input())
    arr = []
    search = []
    for i in range(n):
        arr.append (input())
    q = int(input())
    for i in range(q):
        search.append (input())
    for i in range(q):
        print (findInstanceCount (arr,search[i])


main ()


