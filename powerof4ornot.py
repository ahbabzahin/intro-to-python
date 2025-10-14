def power(n):
    count=0
    if n<=0:
        return False
    if n & (n-1) != 0:
        return False
    while n>1:
        n=n>>1
        count+=1
    return count%2==0
n=int(input("Enter the number: "))
if power(n):
    print(f"{n} is a power of 4")   
else:
    print(f"{n} is not a power of 4")