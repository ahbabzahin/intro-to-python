def find_lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("LCM =", find_lcm(a, b))
