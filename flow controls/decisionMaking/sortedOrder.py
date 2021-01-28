n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
if(n1==n2)&(n2==n3):
    print("numbers are equal")
elif(n1>n2):
    if(n2>n3):
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
else:
    if(n1>n3):
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)