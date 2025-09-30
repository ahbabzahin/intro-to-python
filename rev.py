a=3000
for num in range(1,a+1):
    c=0
    rev=0
    temp=num
    for i in range(1,num+1):
        if(num%i==0):
            c=c+1
    if(c==2):
        while(temp>0):
            dig=temp%10
            rev=rev*10+dig
            temp=temp//10
        if(num==rev):
            print(num,end=" ")