from pydantic import BaseModel


class Address(BaseModel):
    city:str
    state:str
    pincode:int
    

class Patient(BaseModel):
    name: str
    age: int
    gender:str = "Male"
    address:Address
    

address_dict = {'pincode':452001,'city':'Indore','state':'haryana'}


address1 = Address(**address_dict)

patient_dict = {'name':'pawan','age':30,  'address': address1}

patient1 = Patient(**patient_dict)

print(patient1.name)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.model_dump())
print(patient1.model_dump_json())
print(patient1.model_dump(include=['name','age']))
print(patient1.model_dump(exclude=['name']))
print(patient1.model_dump(exclude={'address':['state']}))
print(patient1.model_dump(exclude_unset=True))