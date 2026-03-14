from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field (max_length = 12)
    age: int = Field(gt = 0, le=100)
    email: str = Field(description = "Always @gmail.com", examples = "sanskriti@gmail.com") # type: ignore
    college: str = Field(default = "Masai")

student_info = {'name':'Sanskriti','age': 23, 'email': 'Sanskriti@gmail.com'}
student = Student(**student_info)
print(student.name)
print(student.age)
print(student.email)
print(student.college)
print(student_info)