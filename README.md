# College Management System

A FastAPI-based College Management System to manage students, staff, courses, and books. This system provides RESTful APIs for CRUD operations on each of these entities.

## Features

- **Student Management**: Create, read, update, and delete student records.
- **Staff Management**: Manage college staff including professors and other employees.
- **Course Management**: Handle course details such as title, description, and instructor information.
- **Book Management**: Manage a collection of books in the college library.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the FastAPI app)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/college-management-system.git
    cd college-management-system
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install fastapi uvicorn pydantic
    ```

## Running the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
This will start the server at http://127.0.0.1:8000.```


API Endpoints
Health Check
GET /healthcheck: Check if the API is running.
Student Endpoints
GET /student/{studentId}: Retrieve a student's details by ID.
GET /students: Retrieve all students.
POST /student/{studentId}: Create a new student.
PUT /student/{studentId}: Update an existing student's details.
DELETE /student/{studentId}: Delete a student by ID.
Staff Endpoints
GET /staff/{staffId}: Retrieve staff details by ID.
GET /staff: Retrieve all staff members.
POST /staff/{staffId}: Create a new staff member.
PUT /staff/{staffId}: Update an existing staff member's details.
DELETE /staff/{staffId}: Delete a staff member by ID.
Course Endpoints
GET /course/{courseId}: Retrieve course details by ID.
GET /courses: Retrieve all courses.
POST /course/{courseId}: Create a new course.
PUT /course/{courseId}: Update an existing course's details.
DELETE /course/{courseId}: Delete a course by ID.
Book Endpoints
GET /book/{bookId}: Retrieve book details by ID.
GET /books: Retrieve all books.
POST /book/{bookId}: Create a new book.
PUT /book/{bookId}: Update an existing book's details.
DELETE /book/{bookId}: Delete a book by ID.



### Future Enhancements
Add more features such as department management, class schedules, and student grading.
Implement authentication and authorization for more secure access to the APIs.
### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
### License
This project is licensed under the MIT License - see the LICENSE file for details.
