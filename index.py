# Dictionary to store student records
student_records = {}

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter student roll number: ")
    marks1 = float(input("Enter marks for subject 1: "))
    marks2 = float(input("Enter marks for subject 2: "))

    student_records[roll_no] = {
        'name': name,
        'marks1': marks1,
        'marks2': marks2,
    }
    print("Student record added successfully!")

def display_students():
    print("Student Records:")
    for roll_no, details in student_records.items():
        print(f"Roll Number: {roll_no}, Name: {details['name']}, Marks1: {details['marks1']}, Marks2: {details['marks2']}")

def search_student():
    roll_no = input("Enter the roll number of the student you want to search for: ")
    if roll_no in student_records:
        print(f"Student found!\nRoll Number: {roll_no}, Name: {student_records[roll_no]['name']}, Marks1: {student_records[roll_no]['marks1']}, Marks2: {student_records[roll_no]['marks2']}")
    else:
        print("Student not found!")

def delete_student():
    roll_no = input("Enter the roll number of the student you want to delete: ")
    if roll_no in student_records:
        del student_records[roll_no]
        print("Student record deleted successfully!")
    else:
        print("Student not found!")

def main():
    while True:
        print("\n--- Student Form ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
