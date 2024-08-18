from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

Base = declarative_base()

# SQLAlchemy Models
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    enrollment_date = Column(DateTime, nullable=False)

class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    department = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    publication_date = Column(DateTime, nullable=False)

# Pydantic Schemas
class StudentBase(BaseModel):
    name: str
    address: str
    email: str
    phone: str
    enrollment_date: datetime

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    name: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    enrollment_date: Optional[datetime] = None

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class StaffBase(BaseModel):
    name: str
    position: str
    department: str
    email: str

class StaffCreate(StaffBase):
    pass

class StaffUpdate(StaffBase):
    name: Optional[str] = None
    position: Optional[str] = None
    department: Optional[str] = None
    email: Optional[str] = None

class Staff(StaffBase):
    id: int

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: str
    credits: int

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    title: Optional[str] = None
    description: Optional[str] = None
    credits: Optional[int] = None

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    publication_date: datetime

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    publication_date: Optional[datetime] = None

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
