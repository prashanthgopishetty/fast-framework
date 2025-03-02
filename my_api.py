from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get('/hello')
def hello():
    return "hello world"

students = {
    1: {
        'name':'john',
        'age' : 30,
        'class':'year 12'
    },
    2: {
        'name':'joe',
        'age' : 35,
        'class':'year 11'
    }
}
@app.get('/student/{id}')
def student_info(id : int = Path(..., description="please enter student id", gt=0)):
    return students.get(id)

@app.get('/student-by-name')
def student_by_name(*,name: Optional[str] = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
        else:
            return {"Data": "no details found"}

class Student(BaseModel):
    name:str
    age:int
    year:str

@app.post('/create-student/{student_id}')
def create_student(student_id:int, student: Student):
    if student_id in students:
        return {'error': 'student exist'}
    else:
        students[student_id] = student
        return 'student added successfully'


