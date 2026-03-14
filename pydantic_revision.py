from pydantic import BaseModel, Field, EmailStr,HttpUrl, field_validator

class Student(BaseModel):
    name: str = Field(max_length=20)
    age: int = Field(gt = 0, le = 100)
    mail: EmailStr = Field(description = "give the email in form of @gmail.com", examples = "sanskriti@gmail.com") # type: ignore #Ignore type error 
    college: str = "Masai"
    URL: str

    @field_validator("mail")
    @classmethod
    def email_validator(cls,value):
        domain_name = value.split("@")[-1]
        if domain_name != "gmail.com":
            raise ValueError("Invalid domain provided")
        return value 
    
    @field_validator("college")
    @classmethod
    def college_upper(cls, value):
        return value.upper()
    
student_info = {
    'name': 'Sanskriti',
    'age' : 23,
    'mail': 'sanskriti@gmail.com',
    'URL': 'https://sksksk'
}

student = Student(**student_info)

print(student.name)
print(student.age)
print(student.mail)
print(student.college)
print(student.URL)


