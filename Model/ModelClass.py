from pydantic import BaseModel,EmailStr,AnyUrl,field_validator,Field,computed_field
from typing import List,Dict,Optional,Annotated,Literal


class Address(BaseModel):
    city: str
    pincode: str
    state: str


class Patient(BaseModel):
    patientId: Annotated[str,Field(...,description='Id of the patient',examples=['P001'])]
    name:  Annotated[str,Field(...,description='Name of the patient',examples=['P001'])]
    city: Annotated[str,Field(...,description= 'City of the patient',examples=['Pune'])]
    age: Annotated[int ,Field(...,  gt=0,lt=120,description='Age of the patient',examples=['20,30'])]
    gender: Annotated[Literal['male','female','others'],Field(...,)]
    weight:Annotated[float,Field(...,description='Weight of patient in Mtr',gt=0)]
    height:Annotated[float,Field(...,description='Heaight of the Patient i kgs',gt=0)]
    email:EmailStr
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2) , 2)
        return bmi

    @computed_field
    @property
    def derdict(self) -> str:
        if(self.bmi < 18.5):
            return "UnderWeight"
        elif (self.bmi < 25):
            return "Normal"
        elif(self.bmi<30):
            return "Normal"
        else:
            return "Obese"
    
'''
    @field_validator('email')
    @classmethod
    def email_Validator(cls,value):
        valid_domain = ['hdfc.com','icici.com']
        domainName = value.split('@')[-1]
        if domainName not in valid_domain:
            raise ValueError('Not in a valid domain')
        
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age',mode='after')
    @classmethod
    def valid_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Incorrected age entered')

            
        
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2) , 2)

    @computed_field
    @property
    def derdict(self) -> str:
        if(self.bmi < 18.5):
            return "UnderWeight"
        elif (self.bmi < 25):
            return "Normal"
        elif(self.bmi<30):
            return "Normal"
        else:
            return "Obese"
'''
class updatePatient(BaseModel):
    
    name:  Annotated[Optional[str],Field(default=None)]
    city: Annotated[Optional[str],Field(default=None)]
    age: Annotated[Optional[int] ,Field(default=None,gt=0,lt=120)]
    gender: Annotated[Literal['male','female','others'],Field(default=None)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]
    height:Annotated[Optional[float],Field(default=None,gt=0)]
    email:EmailStr
        
            

