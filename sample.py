from Model.ModelClass import Patient


#patient = Patient()


def insert(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergy)
    print(patient.married)
    print(patient.weight)
    print("Inserted ")

patient_record = {
    "name": "Ravi Verma",
    "age": '10',
    "weight": "72",
    "height": "175",
    "allergy": ["Dust", "Penicillin"],
     "email": "xyz@hdfc.com",
    "contact_Detail": {
        "phone": "+91-9876543210",       
        "city": "Delhi"
    }
}
patien1 = Patient(**patient_record)

insert(patien1)