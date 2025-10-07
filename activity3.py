def numberofbits(n):
    ones=0
    zeroes=0
    while (n):
        if (n & 1):
            ones+=1
        else:
            zeroes+=1
        n=n>>1
    print("Number of 1's are:",ones,"\nNumber of 0's are:",zeroes)
number=int(input("Enter a number:"))
numberofbits(number)