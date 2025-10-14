def compute(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0

n=int(input("Enter a number: "))
if compute(n):
    print(n, "is a power of 2")
else:   
    print(n, "is not a power of 2")