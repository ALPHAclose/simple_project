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

tests:List['Test'] = [
    Test(id=1, name="Mathematics Exam", max_score=100),
    Test(id=2, name="Physics Quiz", max_score=50),
    Test(id=3, name="History Final", max_score=75),
    Test(id=4, name="Computer Science Test", max_score=80),
    Test(id=5, name="English Literature", max_score=90)
]

test_results:List['TestResult'] = []
response_message:List['ResponseMessage'] = []

database = [students, tests, test_results]

@app.post("/students/POST", status_code=status.HTTP_201_CREATED)
async def post_student(student: Student):
    students.append(student)

    return {"message":"Student created successfully"}


@app.get("/students/{student_id}/", status_code=status.HTTP_200_OK)
async def get_student_by_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/students/get_all", status_code=status.HTTP_200_OK)
async def get_all_students():
    if not students:
        raise HTTPException(status_code=404, detail="Students not found")
    return students


@app.post("/tests/POST", status_code=status.HTTP_201_CREATED)
async def post_tests(test: Test):
    tests.append(test)

    return {"message":"Test created successfully"}


@app.get("/tests/{test_id}/", status_code=status.HTTP_200_OK)
async def get_student_by_id(test_id: int):
    for test in tests:
        if test.id == test_id:
            return test
    
    raise HTTPException(status_code=404, detail="Test not found")