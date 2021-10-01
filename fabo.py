n=int(input("Enter the number,that is the limit of Fibonacci serries :"))
j=l=0
k=1
print(k,end=' ')
while(l<=n):
    l=j+k
    if(l<=n):
        print(l,end=' ')
        j=k
        k=l