dict={}
a=int(input())
for i in range(a):
    n=input()
    lst=[]
    for i in range(3):
        mrk=int(input())
        lst.append(mrk)
    dict[n]=lst
slst=[]
print("Sample Output:",end=" ")
klst=dict.keys()
c=0
for i in dict:
    slst=dict[i]
    avg=format((sum(slst)/3),".2f")
    print(f"{i}: {avg}",end=" ")
    c+=1
    if(c!=3):
        print(",",end=" ")
    




