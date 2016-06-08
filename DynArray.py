#!bin/python3

import sys



"""
   Execute Query of form (1 x y) or (2 x y)
   
   SeqList , Querytype 1 or 2, x_val , y_val, lastAns,n


   SeqList  -  Sequence nxn on which the Query has to be run
   Query    -  Query either 1 or 2 based on which index has to be calculated
   x_val    -  x value part of the query e.g 1 x y
   y_val    -  y value part of the query
   lastAns  -  last answer on which the update Query needs to be performed
   n        -  n size

"""

def runQuery (seq,query,x,y,lastAns,n):
   answer = 0
   calc_index = (x ^ lastAns) % n;
   if (calc_index < n and calc_index >=0):
       if (query==1):
          seq[calc_index].append(y)
          return 0 
       elif (query==2):
          answer = seq[calc_index][y%n]
          return answer


"""
   main() is not needed , added to simply block it
   reads n,q and calls RunQuery with the sequence prepared already
"""

def main():
   # read n , q  
   n,q = input().strip().split(' ')
   n,q = int(n),int(q)
   lastAns = 0
   answerlist =[]

   querylist =[]
   seq =[]
   for t in range(n):
      seq.append([])

   for i in range(q):
      qt,x,y = input().strip().split(' ')
      qt,x,y = int(qt),int(x),int(y)
      lastAns = runQuery(seq,qt,x,y,lastAns,n)
      if (qt==2):
         answerlist.append(lastAns)

   for x in answerlist:
      print(x)

"""
    test : method which performs test of main with input from file instead of console
    -- in future we can customize it in better way to make it work with input from file or input from console
    --- in a better way
"""
def test():
   # read n , q  
   n,q = input().strip().split(' ')
   n,q = int(n),int(q)
   lastAns = 0
   answerlist =[]

   querylist =[]
   seq =[]
   for t in range(n):
      seq.append([])

   for i in range(q):
      qt,x,y = input().strip().split(' ')
      qt,x,y = int(qt),int(x),int(y)
      lastAns = runQuery(seq,qt,x,y,lastAns,n)
      if (qt==2):
         answerlist.append(lastAns)

   for x in answerlist:
      print(x)
main()
      
       
   
