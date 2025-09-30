def add_or_update_student(file_name, student_name, intro, subject):
    entry = f"Name: {student_name}, Intro: {intro}, Favorite Subject: {subject}\n"
    with open(file_name, "a") as file:
        file.write(entry)
    print(f"Record for {student_name} added/updated successfully!")

def view_records(file_name):
    try:
        with open(file_name, "r") as file:
            print("\n--- Student Records ---")
            print(file.read())
    except FileNotFoundError:
        print("No records found yet!")

file_name = "students.txt"

while True:
    print("\n1. Add/Update Student")
    print("2. View Records")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        intro = input("Enter brief introduction: ")
        subject = input("Enter favorite subject: ")
        add_or_update_student(file_name, name, intro, subject)
    elif choice == "2":
        view_records(file_name)
    elif choice == "3":
        break
    else:
        print("Invalid choice! Please try again.")
