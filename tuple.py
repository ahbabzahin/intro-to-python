tup=(1,2,3,4,5)
print(tup)
tup=('zahin',1,2,3,4,5)
print(tup)
tup=('mouse',[1,3,4],(1,2,3),3,4)
print(tup)
print(tup[1][2])
print("sliced:", tup[1:3])
tup=('zahin','theo','zarir')
for i in tup:
    print('mr.',i)
tup=(2,3,43,455,5,3)
for i in tup:
    if i %2==0:
        print(i)
    
    
tup=(3,34,4,5,66,4,2,2,4,5,6,6,64,3,3,4,5,7,8,5,4,4,4,4,44,4,4)
x=tup.count(4)
print(x)
y=tup.index(44)
print(y)
tup2=('a','b','c','d','e')
z=tup2+tup
print(z)
