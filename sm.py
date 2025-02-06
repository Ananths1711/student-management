import mysql.connector
con=mysql.connector.connect(host="localhost",port=3306,user="root",password="Ananth.s@12",database="python_db")
cursor=con.cursor()
selectquery="select * from users"
cursor.execute(selectquery)
records=cursor.fetchall()
# Student Management System

# Global list to store student records
students = []


# Function to add a student
def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print(f"Student {name} added successfully!\n")


# Function to view all students
def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No students found.\n")
    else:
        for index, student in enumerate(students, start=1):
            print(f"{index}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()


# Function to update a student
def update_student():
    view_students()
    if students:
        try:
            student_id = int(input("Enter the student number to update: ")) - 1
            if 0 <= student_id < len(students):
                print(f"Updating student: {students[student_id]['name']}")
                name = input("Enter new name (leave blank to keep current): ")
                age = input("Enter new age (leave blank to keep current): ")
                grade = input("Enter new grade (leave blank to keep current): ")

                if name:
                    students[student_id]['name'] = name
                if age:
                    students[student_id]['age'] = int(age)
                if grade:
                    students[student_id]['grade'] = grade

                print("Student updated successfully!\n")
            else:
                print("Invalid student number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


# Function to delete a student
def delete_student():
    view_students()
    if students:
        try:
            student_id = int(input("Enter the student number to delete: ")) - 1
            if 0 <= student_id < len(students):
                deleted_student = students.pop(student_id)
                print(f"Student {deleted_student['name']} deleted successfully!\n")
            else:
                print("Invalid student number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


# Main menu
def main():
    while True:
        print("--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()