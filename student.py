class Student:
    def __init__(self,first_name,last_name,age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def greet(self):
        return f"Hello {self.first_name} {self.last_name} are your full names"

    def initials(self):
        return f"Hello your initials are {self.first_name[0]}{self.last_name[0]}"

    def yob(self):
        year= 2022 - self.age  
        return f"Hello {self.first_name} you were born in the year {year}"
        