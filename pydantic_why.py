from fastapi import FastAPI
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

app = FastAPI()

# pydantic type validation

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=20, title="Enter Patient Name", description="Less than 20 characters",
    examples=['nitish','amit'])]
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    linkdln: AnyUrl
    weight: Annotated[Optional[float], Field(default=None, strict=True, title='weight title')]
    merried: Annotated[bool, Field(default=False, title="Give status of patient if merried or not",
    description="Give status of if merried True or Unmarried False", examples=['True','False'])]
    hieght: float 
    
    contact_details: Dict[str,str]
    allergies: Annotated[Optional[List[str]],Field(default=None, max_length=5)]
    
    @field_validator('email')
    @classmethod
    def email_validate(cls, value):
        domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in domains:
            raise ValueError("Domain did not match")
        else:
            return value 
        
            
    @field_validator('name')
    @classmethod
    def upper_name(cls, value):
        return value.upper() 
    
    @field_validator('age', mode="after")  #for check before after type casting
    @classmethod
    def validate_age(cls, value):
        if value>0 and value <=60:
            return value
        else:
            raise ValueError("Value error")
    
    @model_validator(mode="after")
    def emergency_contact_validate(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            breakpoint()
            raise ValueError("emergency field must be exists when age is above 60")
        return model 
    
    @computed_field
    @property
    def get_bmi(self) -> float:
        bmi = round(self.weight/(self.hieght**2),2)
        return bmi 

patient_info = {'name':'satishkumar','email':'pavan@icici.com','age':'59', 'linkdln':'https://www.linkedin.com',  'contact_details':
{'phone':'578958','emergency':'56859'}, 'allergies':['diriya','maleria'],'weight':60.5, 'hieght':5.2}

patient1 = Patient(**patient_info)

def show_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.merried)
    print(patient.contact_details)
    print(patient.allergies)
    print(type(patient.age))
    print(patient.email)
    print(patient.linkdln)
    print('BMI: ',patient.get_bmi)
    

show_patient(patient1)

# pydantic data validation



    