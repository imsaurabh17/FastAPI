from fastapi import FastAPI, HTTPException
from model import Employee
from typing import List

app = FastAPI()

employee_db: List[Employee] = []

# 1) Return all employee details
@app.get("/employee",response_model=List[Employee])
def emp_detail():
    return employee_db

# 2) Return specific employee details
@app.get("/employee/{id}",response_model=Employee)
def specific_emp(id: int):
    for index,emp in enumerate(employee_db):
        if emp.id == id:
            return employee_db[index]
    raise HTTPException(404,detail = "Employee not found")

# 3) Insert an employee detail
@app.post("/insert/{id}",response_model=Employee)
def insert_emp(new_emp: Employee):
    for index,emp in enumerate(employee_db):
        if new_emp.id == emp.id:
            raise HTTPException(404,detail="Employee already exists")
    
    employee_db.append(new_emp)
    return new_emp

# 4) Update an employee
@app.put("/employee/{id}",response_model=Employee)
def update_emp(id:int, updated_info: Employee):
    for index,emp in enumerate(employee_db):
        if id == emp.id:
            employee_db[index] = updated_info
            return updated_info
    raise HTTPException(404,detail="Employee not found")

# 5) Delete an employee
@app.delete("/employee/{id}",response_model=Employee)
def delete_emp(id:int):
    for index,emp in enumerate(employee_db):
        if emp.id == id:
            del employee_db[index]
    raise HTTPException(404,detail="Employee not found")