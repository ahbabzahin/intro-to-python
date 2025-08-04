try:
    num_str = input("Enter a positive integer: ")

    original_num = int(num_str)

    if original_num < 0:
        print("Please enter a positive integer.")
    else:
        num_digits = len(num_str)
        
        sum_of_powers = 0
        
        for digit_char in num_str:
            digit = int(digit_char)
            sum_of_powers += digit ** num_digits

        if sum_of_powers == original_num:
            print(f"The number {original_num} IS an Armstrong number.")
        else:
            print(f"The number {original_num} IS NOT an Armstrong number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
