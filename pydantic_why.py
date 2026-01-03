from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Dict,Optional

app = FastAPI()

# pydantic type validation

class Patient(BaseModel):
    name: str
    age: int
    wieght: Optional[float] = None 
    merried: Optional[bool] = False 
    contact_details: Dict[str,str]
    allergies: List[str]

patient_info = {'name':'satish','age':'30',  'contact_details':
{'email':'simple@gmail.com', 'phone':'578958'}, 'allergies':['diriya','maleria']}

patient1 = Patient(**patient_info)

def show_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.wieght)
    print(patient.merried)
    print(patient.contact_details)
    print(patient.allergies)
    print(type(patient.age))

show_patient(patient1)

# pydantic data validation



    