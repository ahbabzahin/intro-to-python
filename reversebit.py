def reverseBits(n):
    result = 0
    while n > 0:
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

num = int(input("Enter a number: "))
reversed_num = reverseBits(num)
print("Reversed bit number:", reversed_num)
