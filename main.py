from fastapi import FastAPI, HTTPException
from models import Student, Test, TestResult, ResponseMessage
from starlette import status
from typing import List


app = FastAPI()

students:List['Student'] = [
    Student(id=1, name="Alice Johnson", email="alice@example.com", tests_taken=[85, 90, 78]),
    Student(id=2, name="Bob Smith", email="bob@example.com", tests_taken=[92, 88]),
    Student(id=3, name="Charlie Brown", email="charlie@example.com", tests_taken=[75, 80, 85, 90]),
    Student(id=4, name="David Lee", email="david@example.com", tests_taken=[]),
    Student(id=5, name="Emma Watson", email="emma@example.com", tests_taken=[100, 95, 98])
]

tests:List['Test'] = []
test_results:List['TestResult'] = []
response_message:List['ResponseMessage'] = []

database = [students, tests, test_results]

@app.post("/students/", status_code=status.HTTP_201_CREATED)
async def post_student(student: Student):
    students.append(student)

    return {"message":"Student created successfully"}


@app.get("/students/{student_id}/", status_code=status.HTTP_200_OK)
async def get_student_by_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    
    raise HTTPException(status_code=404, detail="Student not found")
