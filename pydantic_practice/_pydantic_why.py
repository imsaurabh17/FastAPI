# def insert_patients(name:str,age:int):
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print("Inserted")
#     else:
#         raise TypeError


# insert_patients("saurabh",20)

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patients(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr
    linkedin_url : AnyUrl
    age: int
    married: Optional[bool] = 0
    allergies:Optional[List[str]] = Field(default=None,max_length=20)
    contact:Dict[str,str]


p = {"name":"saurabh","age":27,"contact":{'name':'saurabh'},"email":"saurabh@gmail.com","linkedin_url":"https://linkedin.com/123"}

patient1 = Patients(**p)

def insert_patients(patient:Patients):
    print(patient.name,patient.age,patient.married)
    print("inserted")

insert_patients(patient1)
