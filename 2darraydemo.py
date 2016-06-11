#!bin/python3
import sys

minsize = -99999

def findHourGlassSumAtI (arr,i,j):
        sum = 0
        length = len(arr[0])
        #validate the input arrange possible
        # fail fast method
        if (i+2) not in range(length):
                return minsize

        if (j+2) not in range(length):
                return minsize

        # find sum of hourglass at face

        for k in range (3):
                sum += arr[i][j+k]

        #add the hour mid element
        sum += arr[i+1][j+1]

        #add the base sum of hour glass
        for k in range(3):
                sum += arr[i+2][j+k]
        return sum

def findMaxSumofHourGlass (arr):
        max_sum_so_far = minsize
        length = len(arr[0])

        if (len(arr) != length):
                print ('Error , Array not in exact 2d shape !')
                return minsize

        for i in range (length):
                for j in range (length):
                        curr_sum = findHourGlassSumAtI (arr,i,j)
                        if (curr_sum > max_sum_so_far) : max_sum_so_far = curr_sum

        return (max_sum_so_far)

def main ():
        arr = []
        for arr_i in range(6):
           arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
           arr.append(arr_t)
        print (findMaxSumofHourGlass(arr))

main ()
