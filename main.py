from fastapi import FastAPI,Path,Query
import random
from datetime import datetime
from typing import Dict, Union
from typing import Optional
from pydantic import BaseModel

app=FastAPI()


student_details: Dict[int, Dict[str, Union[str, datetime]]] = {
    1: {
        'name': 'John Doe',
        'address': '123 Elm Street, Springfield',
        'email': 'john.doe@example.com',
        'phone': '+1234567890',
        'enrollment_date': datetime(2022, 1, 15)
    },
    2: {
        'name': 'Maaya Patel',
        'address': '456 Oak Avenue, Metropolis',
        'email': 'maaya.patel@example.com',
        'phone': '+0987654321',
        'enrollment_date': datetime(2023, 2, 20)
    },
    3: {
        'name': 'Aditya Singh',
        'address': '789 Maple Lane, Gotham',
        'email': 'aditya.singh@example.com',
        'phone': '+1122334455',
        'enrollment_date': datetime(2021, 3, 25)
    },
    4: {
        'name': 'Rocky Balboa',
        'address': '101 Pine Road, Star City',
        'email': 'rocky.balboa@example.com',
        'phone': '+5566778899',
        'enrollment_date': datetime(2020, 4, 30)
    },
    5: {
        'name': 'Sachin Tendulkar',
        'address': '202 Birch Drive, Sunnydale',
        'email': 'sachin.tendulkar@example.com',
        'phone': '+6677889900',
        'enrollment_date': datetime(2024, 5, 10)
    }
}

class Student(BaseModel):
    name:str
    address:str
    email:str
    phone:str
    enrollment_date:datetime

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    enrollment_date: Optional[datetime] = None


@app.get('/healthcheck')
async def root():
    return "Working"


@app.get('/random')
async def giveMeARandomNumber():
    return random.randrange(100)

@app.get('/studentById/{studentId}')
async def getStudentById(studentId: int = Path(...,description="",gt=0)):
    student=student_details.get(studentId)
    
    if student:
        return student['name']
    else:
        return "Not found"
    # return student_details.get(studentId.get("name"), "Student not found")
    
@app.get('/getAllStudents')
async def getAllStudents():
    return {"data":student_details}
@app.get('/getStudentByName')
async def getStudentByName(*,studentName: Optional[str]= Query(...,description="Student name")):
    flag=0
    for student in student_details.values():
        if student['name'] == studentName:
            return {"data":student}
            break
    if not flag:
        return {"error":"Not found"}

@app.get('/getStudentByIdOrName')
async def getStudentByIdOrName(*,studentId: Optional[int]= Query(None,description=""),studentName:Optional[str]=Query(None,description="")):
    if studentId in student_details:
        return {"data":student_details[studentId]}
    if studentName:
        for student in student_details.values():
            if student['name']==studentName:
                return {"data":student}
            return 
    return {"error":"Not found"}

@app.post('/createStudent/{studentId}')
async def createStudent(*,studentId:int, student:Student):
    if studentId in student_details:
        return {"error":"Student with that Id already exists"}
    student_details[studentId]=student
    print(student_details)
    return student_details[studentId]


@app.post('/updateStudent/{studentId}')
async def updateStudent(*,studentId:int,student:Optional[UpdateStudent]):
    if studentId not in student_details:
        return {"error":"Student with that Id does not exists"}
    if student.name:
        student_details[studentId]['name']=student.name
    if student.address:
        student_details[studentId]['address']=student.address
    if student.email:
        student_details[studentId]['email']=student.email
    if student.phone:
        student_details[studentId]['phone']=student.phone
    if student.enrollment_date:
        student_details[studentId]['enrollment_date']=student.enrollment_date
    return student_details[studentId]
    

@app.delete('/deleteStudent/{studentId}')
async def deleteStudent(*,studentId:int):
    if studentId not in student_details:
        return {"error":"Student with that Id does not exists"}
    student_details.pop(studentId)
    return {"message":"Success"}