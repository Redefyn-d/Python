lst=[]
a=int(input())
for i in range(a):
    name=input()
    lst.append(name)
for j in lst:
    if(lst.count(j)>1):
        lst.remove(j)
print(lst)
