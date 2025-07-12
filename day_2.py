from fastapi import FastAPI
import json

app = FastAPI()

def load_patients():
    with open("patients.json","r") as f:
        return json.load(f)

@app.get("/")
def hello():
    return {"message": "Welcome to the Patient API!"}

@app.get("/about")
def about():
    return {"message": "This API provides information about patients and their conditions."}

@app.get("/view")
def view():
    data = load_patients()
    return data