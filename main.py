from fastapi import FastAPI, Path, Query
from datetime import datetime
from typing import Dict, Union, Optional
from pydantic import BaseModel
import random

app = FastAPI()

# Student Data
student_details: Dict[int, Dict[str, Union[str, datetime]]] = {
    1: {
        'name': 'John Doe',
        'address': '123 Elm Street, Springfield',
        'email': 'john.doe@example.com',
        'phone': '+1234567890',
        'enrollment_date': datetime(2022, 1, 15)
    },
    # Additional students...
}

# Staff Data
staff_details: Dict[int, Dict[str, Union[str, datetime]]] = {
    1: {
        'name': 'Dr. Jane Smith',
        'position': 'Professor',
        'email': 'jane.smith@college.edu',
        'phone': '+11234567890',
        'hire_date': datetime(2015, 8, 23)
    },
    # Additional staff members...
}

# Course Data
course_details: Dict[int, Dict[str, Union[str, datetime]]] = {
    101: {
        'title': 'Physics 101',
        'description': 'Introduction to Physics',
        'instructor': 'Dr. Jane Smith',
        'start_date': datetime(2024, 9, 1)
    },
    # Additional courses...
}

# Book Data
book_details: Dict[int, Dict[str, Union[str, datetime]]] = {
    1001: {
        'title': 'Quantum Mechanics',
        'author': 'Richard Feynman',
        'isbn': '978-0140176000',
        'published_date': datetime(1994, 4, 15)
    },
    # Additional books...
}

# Pydantic Models
class Student(BaseModel):
    name: str
    address: str
    email: str
    phone: str
    enrollment_date: datetime

class Staff(BaseModel):
    name: str
    position: str
    email: str
    phone: str
    hire_date: datetime

class Course(BaseModel):
    title: str
    description: str
    instructor: str
    start_date: datetime

class Book(BaseModel):
    title: str
    author: str
    isbn: str
    published_date: datetime

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    enrollment_date: Optional[datetime] = None

class UpdateStaff(BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    hire_date: Optional[datetime] = None

class UpdateCourse(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    instructor: Optional[str] = None
    start_date: Optional[datetime] = None

class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    published_date: Optional[datetime] = None

# Health Check
@app.get('/healthcheck')
async def root():
    return "Working"

# Random Number
@app.get('/random')
async def giveMeARandomNumber():
    return random.randrange(100)

# Student Endpoints
@app.get('/student/{studentId}')
async def getStudentById(studentId: int = Path(..., description="", gt=0)):
    student = student_details.get(studentId)
    if student:
        return student
    else:
        return {"error": "Student not found"}

@app.get('/students')
async def getAllStudents():
    return {"data": student_details}

@app.post('/student/{studentId}')
async def createStudent(studentId: int, student: Student):
    if studentId in student_details:
        return {"error": "Student with that ID already exists"}
    student_details[studentId] = student.dict()
    return student_details[studentId]

@app.put('/student/{studentId}')
async def updateStudent(studentId: int, student: UpdateStudent):
    if studentId not in student_details:
        return {"error": "Student with that ID does not exist"}
    updated_student = student.dict(exclude_unset=True)
    student_details[studentId].update(updated_student)
    return student_details[studentId]

@app.delete('/student/{studentId}')
async def deleteStudent(studentId: int):
    if studentId not in student_details:
        return {"error": "Student with that ID does not exist"}
    student_details.pop(studentId)
    return {"message": "Student deleted successfully"}

# Staff Endpoints (Similar to Student)
@app.get('/staff/{staffId}')
async def getStaffById(staffId: int = Path(..., description="", gt=0)):
    staff = staff_details.get(staffId)
    if staff:
        return staff
    else:
        return {"error": "Staff not found"}

@app.get('/staff')
async def getAllStaff():
    return {"data": staff_details}

@app.post('/staff/{staffId}')
async def createStaff(staffId: int, staff: Staff):
    if staffId in staff_details:
        return {"error": "Staff with that ID already exists"}
    staff_details[staffId] = staff.dict()
    return staff_details[staffId]

@app.put('/staff/{staffId}')
async def updateStaff(staffId: int, staff: UpdateStaff):
    if staffId not in staff_details:
        return {"error": "Staff with that ID does not exist"}
    updated_staff = staff.dict(exclude_unset=True)
    staff_details[staffId].update(updated_staff)
    return staff_details[staffId]

@app.delete('/staff/{staffId}')
async def deleteStaff(staffId: int):
    if staffId not in staff_details:
        return {"error": "Staff with that ID does not exist"}
    staff_details.pop(staffId)
    return {"message": "Staff deleted successfully"}

# Course Endpoints (Similar to Student)
@app.get('/course/{courseId}')
async def getCourseById(courseId: int = Path(..., description="", gt=0)):
    course = course_details.get(courseId)
    if course:
        return course
    else:
        return {"error": "Course not found"}

@app.get('/courses')
async def getAllCourses():
    return {"data": course_details}

@app.post('/course/{courseId}')
async def createCourse(courseId: int, course: Course):
    if courseId in course_details:
        return {"error": "Course with that ID already exists"}
    course_details[courseId] = course.dict()
    return course_details[courseId]

@app.put('/course/{courseId}')
async def updateCourse(courseId: int, course: UpdateCourse):
    if courseId not in course_details:
        return {"error": "Course with that ID does not exist"}
    updated_course = course.dict(exclude_unset=True)
    course_details[courseId].update(updated_course)
    return course_details[courseId]

@app.delete('/course/{courseId}')
async def deleteCourse(courseId: int):
    if courseId not in course_details:
        return {"error": "Course with that ID does not exist"}
    course_details.pop(courseId)
    return {"message": "Course deleted successfully"}

# Book Endpoints (Similar to Student)
@app.get('/book/{bookId}')
async def getBookById(bookId: int = Path(..., description="", gt=0)):
    book = book_details.get(bookId)
    if book:
        return book
    else:
        return {"error": "Book not found"}

@app.get('/books')
async def getAllBooks():
    return {"data": book_details}

@app.post('/book/{bookId}')
async def createBook(bookId: int, book: Book):
    if bookId in book_details:
        return {"error": "Book with that ID already exists"}
    book_details[bookId] = book.dict()
    return book_details[bookId]

@app.put('/book/{bookId}')
async def updateBook(bookId: int, book: UpdateBook):
    if bookId not in book_details:
        return {"error": "Book with that ID does not exist"}
    updated_book = book.dict(exclude_unset=True)
    book_details[bookId].update(updated_book)
    return book_details[bookId]

@app.delete('/book/{bookId}')
async def deleteBook(bookId: int):
    if bookId not in book_details:
        return {"error": "Book with that ID does not exist"}
    book_details.pop(bookId)
    return {"message": "Book deleted successfully"}

