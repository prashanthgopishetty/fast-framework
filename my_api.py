from fastapi import FastAPI, Path

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
