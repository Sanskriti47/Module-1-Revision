# python -m install install fastapi pydantic uvicorn 
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/hello")
def say_hello():
    return "Hello, Sanskriti!"

@app.get("/bye")
def say_bye():
    return "Bye, Sanskriti!"

# After running this on one terminal, open a new terminal to see the server base
# to check the server base type uvicorn main:app (main is basically the file name that you have provided)
# the app is basically the function that you have defined in the FastAPI function in your project
# app = FastAPI() ---> 


# Important in order to run the server in the terminal type python -m uvicorn main:app --reload
# When you make changes to the return value, make sure you save the file
# Then close the server (ctrl+C)
# Restart the server 
# Refresh the output page 

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