n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
if(n1==n2)&(n2==n3):
    print("numbers are equal")
elif(n1>n2):
    if(n1<n3):
        print(n1)
    else:
        print(n3)
else:
    if(n2<n3):
        print(n2)
    else:
        print(n3)
