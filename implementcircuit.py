

def circuit_output(A, B, C):
    Q = (A & B) | C
    return Q


A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
C = int(input("Enter C (0 or 1): "))

print("Output Q =", circuit_output(A, B, C))
