from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator


class Student(BaseModel):
    name: str
    age: int
    email: EmailStr
    college: str

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        domain_name = value.split("@")[-1]
        if domain_name != "gmail.com":
            raise ValueError("Invalid domain")
        return value

    @field_validator("college")
    @classmethod
    def converting_college(cls, value):
        return value.lower()


student_info = {
    'name': 'Sanskriti',
    'age': 23,
    'email': 'sanskriti@gmail.com',
    'college': 'MASAI'
}

student = Student(**student_info)

print(student.name)
print(student.age)
print(student.email)
print(student.college)