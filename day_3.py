# -------------------- path & query functions-------------------------

from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_patients():
    with open("patients.json","r") as f:
        return json.load(f)
    

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str = Path(...,description="Enter the patiend_id",example="P01")):
    data = load_patients()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")


@app.get("/view")
def view_patients(sort_by:str=Query(...,description="Select either name, age or condition",example="name"),order:str=Query('asc',description="sort either in asc or desc order")):

    validation = ['name','age','condition']

    if sort_by not in validation:
        raise HTTPException(status_code=400,detail = f"Select only from {validation}")
    
    if order not in ['asc',"desc"]:
        raise HTTPException(status_code=400, description="select either asc or desc")
    
    data = load_patients()

    order_by = False if order=="asc" else True
    
    sort = sorted(data.values(), key = lambda x:x.get(sort_by),reverse = order_by)

    return sort