num=int(input('input a number to check armstrong or not:'))
result=0
temp=num
while temp!=0:
    digit=temp%10
    result+=digit**3
    temp//=10
if num==result:
    print(f'{num} is an armstrong number')                             
else:
    print(f'{num} is not an armstrong number')