from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

# Load students data from the json file
def load_students_data():
    with open('students.json', 'r') as f:
        students_data = json.load(f)
        
    return students_data

# Get all the students.
# end point /students
@app.get("/students")
def get_all_student():
    return load_students_data()
# Want all the students data from the json file.


# Want any one particular student data 
# Path parameter is passed via {}
@app.get("/students/{students_id}")
def get_student_with_id(students_id: str = Path(...,description="ID of the student to access, example "ST01")):
    data = load_students_data()

    if students_id not in data:
        raise HTTPException(status_code=404,detail="Student with this id not present")
    
    return data[students_id]

# /docs gives us the list of api in our browser 
# status code 404 is for not found 
# To give description we make use of pat, path with ... three dots means mandatory parameter, but you have to import it from fastapi


# Query parameter 
# /students?students_id=ST01
# Import Query from fastapi
@app.get("/studentss")
def get_student_with_id(students_id: str =  Query(...,description="Students_id",example="?ST02")):
    data = load_students_data()

    if students_id not in data:
        raise HTTPException(status_code=404,detail="Student with this id not present")
    
    return data[students_id]