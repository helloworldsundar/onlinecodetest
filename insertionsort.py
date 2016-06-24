#insertion sort demo

def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        ccard = arr[i]
        print(ccard)
        j = i
        while (j >= 0):
            if arr[j-1] > ccard:
                arr[j] = arr[j-1]
                j = j - 1
            else:
                break
        arr[j] = ccard
    return arr

def sort (arr,type):
    if(type=='insertionsort'):
        return insertionsort(arr)
    else:
        return arr


def main():
    n = int(input("get N: "))
    arr=[]
    for i in range(n):
        arr.append(int(input(str(i)+": ")))
    print('Sorting :\n')
    arr = sort(arr,'insertionsort')
    for x in arr:
        print(x,end=' ')

main()

