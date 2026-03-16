from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: int
    college: str = 'Masai'
    contact: Optional[str] = Field(default='none', min_length=10, max_length=10)

student_info = {
    'name':'Sanskriti',
    'age': 23
}

student = Student(**student_info)

print(student)