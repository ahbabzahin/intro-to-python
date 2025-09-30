def binary_to_decimal(binary_str):
    
    decimal = int(binary_str, 2)
    return decimal


binary_input = input("Enter a binary number: ")
try:
    print("Decimal value:", binary_to_decimal(binary_input))
except ValueError:
    print("Invalid input! Please enter only 0s and 1s.")
