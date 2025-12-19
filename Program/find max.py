a=int(input())
max=0
lst=[]
for i in range (a):
    x=int(input())
    if(x>max):
        max=x
    lst.append(x)
print(max)
