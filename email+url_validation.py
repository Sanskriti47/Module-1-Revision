from pydantic import BaseModel, Field, EmailStr, HttpUrl

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr
    URL: HttpUrl
    college: str = "Masai"

student_info = {'name':'Sanskriti', 'age':23, 'email':'sanskriti@gmail.com', 'URL':'http:/ggjyg'}
student = Student(**student_info)

print(student_info)
print(student.college)