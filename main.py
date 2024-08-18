from fastapi import FastAPI, Path, Depends
from typing import List
from datetime import datetime
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models

app = FastAPI()

# Initialize the database
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Health Check
@app.get('/healthcheck')
async def healthcheck():
    return {"status": "Working"}

# Random Number
@app.get('/random')
async def random_number():
    import random
    return {"number": random.randrange(100)}

# Student Endpoints
@app.get('/students', response_model=List[models.Student])
async def get_all_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

@app.get('/student/{studentId}', response_model=models.Student)
async def get_student_by_id(studentId: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == studentId).first()
    if student:
        return student
    else:
        return {"error": "Student not found"}

@app.post('/student/{studentId}', response_model=models.Student)
async def create_student(studentId: int, student: models.StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == studentId).first()
    if db_student:
        return {"error": "Student with that ID already exists"}
    
    new_student = models.Student(id=studentId, **student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.put('/student/{studentId}', response_model=models.Student)
async def update_student(studentId: int, student: models.StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == studentId).first()
    if not db_student:
        return {"error": "Student not found"}

    for key, value in student.dict(exclude_unset=True).items():
        setattr(db_student, key, value)
    
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete('/student/{studentId}')
async def delete_student(studentId: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == studentId).first()
    if not db_student:
        return {"error": "Student not found"}

    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}

# Staff Endpoints
@app.get('/staff', response_model=List[models.Staff])
async def get_all_staff(db: Session = Depends(get_db)):
    staff = db.query(models.Staff).all()
    return staff

@app.get('/staff/{staffId}', response_model=models.Staff)
async def get_staff_by_id(staffId: int, db: Session = Depends(get_db)):
    staff = db.query(models.Staff).filter(models.Staff.id == staffId).first()
    if staff:
        return staff
    else:
        return {"error": "Staff not found"}

@app.post('/staff/{staffId}', response_model=models.Staff)
async def create_staff(staffId: int, staff: models.StaffCreate, db: Session = Depends(get_db)):
    db_staff = db.query(models.Staff).filter(models.Staff.id == staffId).first()
    if db_staff:
        return {"error": "Staff with that ID already exists"}
    
    new_staff = models.Staff(id=staffId, **staff.dict())
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

@app.put('/staff/{staffId}', response_model=models.Staff)
async def update_staff(staffId: int, staff: models.StaffUpdate, db: Session = Depends(get_db)):
    db_staff = db.query(models.Staff).filter(models.Staff.id == staffId).first()
    if not db_staff:
        return {"error": "Staff not found"}

    for key, value in staff.dict(exclude_unset=True).items():
        setattr(db_staff, key, value)
    
    db.commit()
    db.refresh(db_staff)
    return db_staff

@app.delete('/staff/{staffId}')
async def delete_staff(staffId: int, db: Session = Depends(get_db)):
    db_staff = db.query(models.Staff).filter(models.Staff.id == staffId).first()
    if not db_staff:
        return {"error": "Staff not found"}

    db.delete(db_staff)
    db.commit()
    return {"message": "Staff deleted successfully"}

# Course Endpoints
@app.get('/courses', response_model=List[models.Course])
async def get_all_courses(db: Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return courses

@app.get('/course/{courseId}', response_model=models.Course)
async def get_course_by_id(courseId: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == courseId).first()
    if course:
        return course
    else:
        return {"error": "Course not found"}

@app.post('/course/{courseId}', response_model=models.Course)
async def create_course(courseId: int, course: models.CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == courseId).first()
    if db_course:
        return {"error": "Course with that ID already exists"}
    
    new_course = models.Course(id=courseId, **course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@app.put('/course/{courseId}', response_model=models.Course)
async def update_course(courseId: int, course: models.CourseUpdate, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == courseId).first()
    if not db_course:
        return {"error": "Course not found"}

    for key, value in course.dict(exclude_unset=True).items():
        setattr(db_course, key, value)
    
    db.commit()
    db.refresh(db_course)
    return db_course

@app.delete('/course/{courseId}')
async def delete_course(courseId: int, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == courseId).first()
    if not db_course:
        return {"error": "Course not found"}

    db.delete(db_course)
    db.commit()
    return {"message": "Course deleted successfully"}

# Book Endpoints
@app.get('/books', response_model=List[models.Book])
async def get_all_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books

@app.get('/book/{bookId}', response_model=models.Book)
async def get_book_by_id(bookId: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == bookId).first()
    if book:
        return book
    else:
        return {"error": "Book not found"}

@app.post('/book/{bookId}', response_model=models.Book)
async def create_book(bookId: int, book: models.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == bookId).first()
    if db_book:
        return {"error": "Book with that ID already exists"}
    
    new_book = models.Book(id=bookId, **book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.put('/book/{bookId}', response_model=models.Book)
async def update_book(bookId: int, book: models.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == bookId).first()
    if not db_book:
        return {"error": "Book not found"}

    for key, value in book.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete('/book/{bookId}')
async def delete_book(bookId: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == bookId).first()
    if not db_book:
        return {"error": "Book not found"}

    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}
