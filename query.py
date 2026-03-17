# Query parameter 
# /students?students_id=ST01
# Import Query from fastapi
from fastapi import FastAPI, HTTPException, Query
import json

app = FastAPI()

def load_students_data():
    with open("students.json", "r") as f:
        students_data = json.load(f)
    return students_data


@app.get("/students")
def get_student_with_id(
    students_id: str = Query(..., description="Students id", example="ST02")
):
    data = load_students_data()

    if students_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Student with this id not present"
        )

    return data[students_id]