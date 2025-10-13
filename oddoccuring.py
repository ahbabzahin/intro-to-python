def oddoccuring(arr):
    res=0
    for i in arr:
        res=res^i
    return res
arr=[]
n=int(input('enter array size:'))
while(n):
    num=int(input('enter num:'))
    arr.append(num)
    n=n-1
print('odd occurence num is:',oddoccuring(arr))