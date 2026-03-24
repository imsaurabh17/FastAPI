from fastapi import FastAPI, HTTPException
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

@app.get("/get_students",response_model=List[Student])
def get_students():
    return Student_db

@app.get("/get_specific_student",response_model=Student)
def get_specific_student(id: int):

    if id not in Student_db:
        for index, student in enumerate(Student_db):
            if student["id"] == id:
                return student
            
    raise HTTPException(status_code=404,detail="Student not found")

@app.put("/update_student", response_model=Student)
def update_student(id:int, updated_data: Student):
    for student in Student_db:
        if student["id"] == id:
            student["name"] = updated_data.name
            student["email"] = updated_data.email
            student["age"] = updated_data.age
            student["branch"] = updated_data.branch

        return student

    raise HTTPException(status_code=404,detail="Student not found")