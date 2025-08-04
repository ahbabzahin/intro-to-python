try:
    n_terms = int(input("Enter the number of terms for the Fibonacci series: "))

    if n_terms <= 0:
        print("Please enter a positive integer.")
    elif n_terms == 1:
        print("Fibonacci series:")
        print(0)
    else:
        a, b = 0, 1
        count = 0
        print("Fibonacci series:")
        while count < n_terms:
            print(a)
            nth = a + b
            a = b
            b = nth
            count += 1

except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
