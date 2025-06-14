from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from Model.ModelClass import Patient,updatePatient
import json
from Logger.logger import logger

logger.info("Sartint the Api...")

app = FastAPI()

@app.get("/")
def initiate():
    return {"Message":"Patient Manegment site"}

@app.get("/Info")
def patientInfo():
    with open('patient.json',"r") as f:
        data = json.load(f)
    return data

@app.get("/View")
def InfoView():
    data = patientInfo()
    return data

@app.get("/patient/{id}")
def patientInfoForId(id: str = Path(...,description='Thie field used to find patient id in db',example="patient1")):
    print("Inside the patientinfo")
    data = patientInfo()
    print("Getting data Sucessfully :")
    print("The patient id is :"+ id)
    if id in data:
        return data[id]    
    raise HTTPException(status_code=404,detail="Patient Not Found") 

@app.get("/sort")
def sortPatient(sortBy: str = Query(...,description="Sort patient by height,weight,bms"),order: str= Query('asc',description='sort asc or desc')):
    validField = ['height','weight','bmi']
    if sortBy  not in validField:
        raise HTTPException(400,detail=f"Invalid field select for the sort : {validField}")
    if order not in ['asc','desc']:
        raise HTTPException(400,detail=f"Invalid field select order{validField}")
        
    data = patientInfo()
    orderBool = True if order == "desc" else False
    sortedData = sorted(data.values(),key=lambda k: k.get(sortBy,0),reverse=orderBool)
    return sortedData

def SaveData(data):
    try:
        logger.info("Inside Save Data")
        with open('patient.json','w') as w:
            json.dump(data,w)
    except Exception as ex:
        logger.info("Error while avinf the new patient data in the file")
        logger.info(ex)
        


@app.post("/addPatient")
def addPatient(patient: Patient):
    logger.info("inside the addPatient method")
    #load Exsisting data 
    patientData = patientInfo()
    logger.info("Exsisting patient record read sucessfully")


    #Check it exsist or  not 
    if patient.patientId in patientData:
        logger.info("Patient already exsist")
        raise HTTPException(detail='patient already exists',status_code=400)
    
    # new patient add 
    
    patientData[patient.patientId] = patient.model_dump(exclude=['patientId'])
    logger.info(f"New patien of the patientId: {patient.patientId} is added")

    #Save to the file 
    SaveData(patientData)

    return JSONResponse(status_code=201,content={'Message :New Patient added sucessfully'})

@app.put('/edit/{patient_id}')
def Update_Patient_Record(patient_id : str,patient_Update: updatePatient):
    #load data
    data = patientInfo()

      #Check it exsist or  not 
    if patient_id not in  data:
        logger.info("Patient not exsist")
        raise HTTPException(detail='patient Not exists',status_code=400)
    exsisting_patient = data[patient_id]

    updatedPatientRecord = patient_Update.model_dump(exclude_unset=True)

    for key,value in updatedPatientRecord.items():
        exsisting_patient[key] = value

    exsisting_patient["patientId"] = patient_id
    patient_pydantic_obj = Patient(**exsisting_patient)
    patient_pydantic_obj.model_dump(exclude='patientId')

    data[patient_id]=exsisting_patient

    #save the data 
    SaveData(data)

    return JSONResponse(status_code = 200,content=f"The patient record updated sucessfully id : {patient_id}")

@app.delete("/delete/{id}")
def Delete_patient(id: str):
    data  = patientInfo()
      #Check it exsist or  not 
    if id not in  data:
        logger.info("Patient not exsist")
        raise HTTPException(detail='patient Not exists',status_code=400)
    del data[id]

    SaveData(data)

    return JSONResponse(status_code = 200,content=f"The patient record deleted sucessfully id : {id}")












