
try:
    marks = float(input(" "))
    if not (0 <= marks <= 100):
        print("Invalid marks. ")
    else:
        attendance = float(input("Enter your attendance percentage : "))
        if not (0 <= attendance <= 100):
            print("Invalid attendance")
        else:
            min_marks_for_eligibility = 50
            min_attendance_for_eligibility = 75

            if marks >= min_marks_for_eligibility and attendance >= min_attendance_for_eligibility:
                print(" eligible.")
            elif marks < min_marks_for_eligibility and attendance < min_attendance_for_eligibility:
                print(" not eligible ")
            elif marks < min_marks_for_eligibility:
                print("not eligible")
            else:
                print(" not eligible.")

except ValueError:
    print("Invalid input. Please enter numeric values for marks and attendance.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")