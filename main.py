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

test_results: List[TestResult] = [
    TestResult(student_id=1, test_id=1, score=85),
    TestResult(student_id=1, test_id=2, score=90),
    TestResult(student_id=1, test_id=3, score=78),
    
    TestResult(student_id=2, test_id=1, score=92),
    TestResult(student_id=2, test_id=2, score=88),
    
    TestResult(student_id=3, test_id=1, score=75),
    TestResult(student_id=3, test_id=2, score=80),
    TestResult(student_id=3, test_id=3, score=85),
    TestResult(student_id=3, test_id=4, score=90),
    
    TestResult(student_id=5, test_id=1, score=100),
    TestResult(student_id=5, test_id=2, score=95),
    TestResult(student_id=5, test_id=3, score=98),
]

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


@app.get("/tets/get_all", status_code=status.HTTP_200_OK)
async def get_all_tests():
    if not tests:
        raise HTTPException(status_code=404, detail="Students not found")
    return tests


@app.post("/results/", status_code=status.HTTP_201_CREATED)
async def post_results(result: TestResult):
    test_results.append(result)
    return {"message":"TestResults created successfully"}


@app.get("/results/student/{student_id}")
async def get_results_from_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student.tests_taken
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/results/test/{test_id}/")
async def get_all_test_results_for_a_specific_test(test_id: int):
    list_to_return = []

    for test in test_results:
        if test.id == test_id:
            list_to_return.append(test)
    
    if not list_to_return:
        raise HTTPException(status_code=404, detail="Tests not found")
    
    return list_to_return

@app.get("/results/test/{test_id}/average")
async def get_average_score(test_id: int):
    sum_of_scores = 0
    count = 0

    for test in test_results:
        if test.id == test_id:
            sum_of_scores += test.score
            count += 1

    if sum_of_scores:
        raise HTTPException(status_code=404, detail="Tests not found")
    
    average = sum_of_scores / count
    
    return {"message":"successfully", "average": average}

@app.get("/results/test/{test_id}/highest")
async def get_highest_score(test_id: int):
    scores = []

    for test in test_results:
        if test.id == test_id:
            scores.append(test.score)

    if not scores:
        raise HTTPException(status_code=404, detail="Tests not found")
    
    scores = scores.sort(reverse=True)

    return {"message":"successfully", "highest":scores[0]}

@app.get("/students/{student_id}")
async def delete_student_by_id(student_id: int):
    index = 0

    for student in range(len(students)):
        if students[student].id == student_id:
            index = student
        
    if not index:
        raise HTTPException(status_code=404, detail="Student not found")
    
    students.pop(index)

    return {"message":"successfully","students":students}

