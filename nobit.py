def noofbit(n):
    count=0
    while(n):
        count+=1
        n=n>>1
    return count
n=int(input("Enter a number:"))
print("Number of bits required to represent the number in binary:",noofbit(n))