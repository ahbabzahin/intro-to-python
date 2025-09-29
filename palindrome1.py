no=int(input("enter no"))
origno=no
revno=0
while no>0:
    dig=no%10
    revno=revno*10+dig
    no=no//10
if origno==revno:
    print("palindrome")     
else:
    print("not palindrome")