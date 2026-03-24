from fastapi import FastAPI
from crud.models import Student
from typing import List
from itertools import count

app = FastAPI(title="Student details")

Student_db: List[Student] = []

id_count = count(start=1)

@app.post("/students")
def add_student(student: Student):
    id = next(id_count)

    student_data = {
        "id": id,
        "name": student.name,
        "email": student.email,
        "age": student.age,
        "branch": student.branch
    }

    Student_db.append(student_data)

    return student_data
