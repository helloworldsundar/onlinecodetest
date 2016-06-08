#!/bin/python3

# Factorial program using recursion

"""
    name : factorial
    input : n
    output : n! which is n x (n-1)!

    Explanation :

        This function is a recursive fn which calls itself to determine
        the factorial of given value of n in top down manner.

"""
def factorial(n):
    if (n<=1):
        return 1
    else:
        return (n*factorial(n-1))


def main():
    #read the input
    n=int(input())
    print (factorial(n))

main()

