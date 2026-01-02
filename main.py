from fastapi import FastAPI,Path, HTTPException,Query
import json

app = FastAPI()

@app.get('/')
def home():
    return {'msg':'home page'}
        
def load_data():
    f=open('patient.json',"r")
    data=json.load(f)
    return data        

@app.get('/patients')
def patients():
    data = load_data()
    return data 


@app.get('/patient/{patient_id}')
def get_patient(patient_id: str = Path(..., description="Id of the patient in the DB", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient Not Found!")
 

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of hieght, weigth or bmi'),
order: str = Query('asc', description="sort in the desc order")):
    valid_fields = ['hieght','weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid fields select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f'Invalid order select between asc and desc')

    data = load_data()
    
    sort_order = True if order=='desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)
    
    return sorted_data
    
