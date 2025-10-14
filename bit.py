n = int(input("Enter number: "))

if n == 0:
    print("No set bit present.")
else:
    position = (n & -n).bit_length()
    print("Position of the first set bit:", position)
