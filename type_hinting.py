def student_details(name: str, age: int, gender: str, college: str):
    if type(name) == str and type(age) == int and isinstance(gender, str) and gender in ("male", "female") and type(college) == str:
        print(name)
        print(age)
        print(gender)
        print(college)
    else:
        raise TypeError("Invalid data")

student_details("Sanskriti", 23, "female", "masai")