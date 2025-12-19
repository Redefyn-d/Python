temp=float(input("Enter the input:\n"))
print(temp)
t=input("Enter the temprature is in F or C:\n")
print(t)
if(t.lower()=='f'):
    if(temp>=100.4):
        print("The user has fever")
    else:
        print("The user does not have fever")
elif(t.lower()=='c'):
    if(temp>=38):
        print("The user has fever")
    else:
        print("The user does not have fever")
