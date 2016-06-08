n=int(input())

phonebook={}

for i in range(n):
    name,phonenum=input().strip().split(' ')
    phonebook[name]=phonenum

for i in range(n):
    search=input()
    if (search in phonebook):
        print (search+'='+phonebook[search])
    else:
        print ('Not found')


