n=int(input("Enter the limit of Fibonacci serries :"))
j=0
k=1
print(k,end=' ')
while(l<=n):
    l=j+k
    if(l<=n):
        print(l,end=' ')
        j=k
        k=l
