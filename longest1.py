def longest_consecutive_ones(n):

    binary = bin(n)[2:]

    longest = max(len(seq) for seq in binary.split('0'))
    return longest


num = int(input("Enter a number: "))

print("Longest consecutive 1’s in binary:", longest_consecutive_ones(num))
