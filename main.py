from fastapi import FastAPI,Path, HTTPException
import json



app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Pavan"}

@app.post("/create-user")
def create_user(data: dict):
 return {"status": "success", "data": data}

@app.get("/hello")
def hello():
    return {'message': 'hello'}

def load_students():
    f=open('student.json',"r")
    data=json.load(f)
    return data 

@app.get('/view')
def view():
    data = load_students()
    return data 

@app.get('/student/{student_id}')
def view_student(student_id: int = Path(..., description="Enter the student ID", example="Like 1,2,3")):
    data = load_students()
    # breakpoint()
    for i in data['students']:
        if i['id']==student_id:
            return i
    raise HTTPException(status_code=404, det='student not found!')


@app.get('/patients')
def load_patient_data():
    f=open('patient.json',"r")
    data = json.load(f)
    return data

@app.get('/patient/{patient_id}')
def filter_patient(patient_id: int = Path(..., description='Enter Patient Id', example='1,2,3')):
    data  = load_patient_data()
    for patient in data['patients']:
       if patient['patient_id']==patient_id:
           return patient
    return HTTPException(status_code=200, detail="Patient Not Found!")


def load_data():
    f=open('patient.json',"r")
    data=json.load(f)
    return data

@app.get('/load/{patient_id}')
def datas(patient_id: int = Path(..., description='Compalsory id', example='123')):
    data = load_data()
    for patient in data['patients']:
        if patient['patient_id']==patient_id:
            return patient
    else:
        return {'data': 'patient not found!'}
    






 

        

