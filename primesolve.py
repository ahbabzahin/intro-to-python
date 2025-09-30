def primesolve(n):
    prime=[True for i in range(n+1)]
    currentnumber=2
    while(currentnumber*currentnumber<=n):
        if(prime[currentnumber]==True):
            for i in range(currentnumber*currentnumber,n+1,currentnumber):
                prime[i]=False
        currentnumber+=1
    prime[0]=prime[1]=False
    for i in range(n+1):
        if(prime[i]):
            print(i,end=" ")
n=int(input("Enter a number: "))
primesolve(n)   
print("following are the prime numbers smaller than or equal to",n)