def myfunction1(n):
    if n <= 0:
        return
    for i in range(0, n+1):
        print("Codingal")
    myfunction1(n//2)
    myfunction1(n//3)

# Recurrence: T(n) = T(n/2) + T(n/3) + O(n)
# Time Complexity: O(n log n)


def myfunction2(n):
    if n <= 1:
        return
    print("Codingal")
    myfunction2(n-1)

# Recurrence: T(n) = T(n-1) + O(1)
# Time Complexity: O(n)


if __name__ == "__main__":
    print("Recurrence and Time Complexity Results:\n")
    print("myfunction1:")
    print("T(n) = T(n/2) + T(n/3) + O(n)")
    print("Time Complexity = O(n log n)\n")

    print("myfunction2:")
    print("T(n) = T(n-1) + O(1)")
    print("Time Complexity = O(n)")
