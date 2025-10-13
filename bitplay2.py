def checksame(num1,num2):
    if ((num1^num2)!=0):
        print('not same')
    else:
        print('same')
num1=int(input('enter num1:'))
num2=int(input('enter num2:'))  
checksame(num1,num2)