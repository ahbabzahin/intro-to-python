def multiply_one_iteration(n, m):
    # Direct multiplication
    return n * m

def multiply_n_iterations(n, m):
    # Using repeated addition
    result = 0
    for _ in range(m):
        result += n
    return result

# Example usage
n = 5
m = 4
print("One iteration result:", multiply_one_iteration(n, m))
print("N iterations result:", multiply_n_iterations(n, m))
