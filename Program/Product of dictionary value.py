dict={}
a=int(input("Enter the number of elements in dict"))
for i in range(a):
    p=input()
    q=int(input())
    dict[p]=q
prd=1
for i in dict:
    prd*=dict[i]
print()
print(prd)
