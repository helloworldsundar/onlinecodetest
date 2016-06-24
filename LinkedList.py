#Linked List in python

#Node Defintion
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

#Solution Defintion
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
        current= head
        if (head==None):
            return Node(data)
        while current.next:
            current = current.next
        current.next=Node(data)
        return head



mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);

