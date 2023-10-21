class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:

# Create a list of Student objects
students = [
    Student("Alice", "A101", 3.9),
    Student("Bob", "B202", 3.7),
    Student("Charlie", "C303", 4.0),
    Student("David", "D404", 3.5),
]

# Sort the list of students by CGPA in descending order
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
