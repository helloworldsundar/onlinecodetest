n=int(input())
s=[]
for i in range(n):
    s.append(input())


for k in range(n):
    str1= ''
    str2= ''
    for i in range(len(s[k])):
        if (i%2==0):
            str1=str1+s[k][i]
        else:
            str2=str2+s[k][i]
    print (str1 +' '+str2)