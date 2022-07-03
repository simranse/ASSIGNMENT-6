#Program1: Perfect Number....

def Perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if (n==sum) and ((sum+n)/2):
        print(" The number is Perfect")
    else:
        print(" The number is not Perfect")
n=int(input("Enter a number: "))
Perfect(n)

