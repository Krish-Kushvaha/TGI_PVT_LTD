students = []

def add_student(student_id, name, marks):
    student_record = {
        "ID": student_id,
        "Name": name,
        "Marks": marks
    }

    students.append(student_record)

def show_students():
    print("\nStudent Records:\n")

    for student in students:
        student_info = (
            student["ID"],
            student["Name"],
            student["Marks"]
        )  

        print(f"ID: {student_info[0]}")
        print(f"Name: {student_info[1]}")
        print(f"Marks: {student_info[2]}")
        print("-" * 20)

add_student(1, "Krish", 85)
add_student(2, "Rohan", 78)
add_student(3, "Neha", 92)

show_students()