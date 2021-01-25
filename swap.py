#swap
n1=int(input("num1: "))
n2=int(input("num2: "))
n3=0
n3=n1
n1=n2
n2=n3
print("n1=",n1,"n2=",n2)
#without temporory variable
n1=n1+n2
n2=n1-n2
n1=n1-n2
print(n1,n2)