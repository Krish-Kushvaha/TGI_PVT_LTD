# student_manager.py
students = {}

def add_student(name, marks):
    students[name] = {"marks": marks, "grade": get_grade(marks)}

def get_grade(marks):
    if marks >= 90: return "A"
    elif marks >= 75: return "B"
    elif marks >= 60: return "C"
    else: return "F"

def show_all():
    for name, data in students.items():
        print(f"{name}: {data['marks']} ({data['grade']})")

add_student("Alice", 92)
add_student("Bob", 78)
show_all()