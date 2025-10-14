def compute(x,y):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x
        y>>=1
    else:
        result *= x
        y=y-1
    return result
x=int(input("Enter the base: "))
y=int(input("Enter the exponent: "))
print(f"{x} raised to the power {y} is {compute(x,y)}")