from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    college: str

student_info = {'name':'Sanskriti', 'age':23, 'college':'Masai'}  
student = Student(**student_info)  

print(student.name)
print(student.age)
print(student.college)
