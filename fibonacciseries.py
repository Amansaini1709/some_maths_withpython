#fibonacci series
a=0
b=1
n=int(input("enter the no. of terms you want to be printed"))
print(a)
print(b)
for i in range(1,n-1,1):
    c=a+b
    a=b
    b=c
    print (c)
