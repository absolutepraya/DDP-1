class Person:
    # Class attribute
    def __init__(self, name:str, surname:str):
        self.name = name
        self.surname = surname
    
    # Edit information for name and surname of the person
    def editInfo(self, name:str, surname:str):
        self.name = name
        self.surname = surname

class Course:
    # Class attribute
    def __init__(self, name:str, sks:int):
        self.name = name
        self.sks = sks

class Student(Person):
    # Class attribute
    def __init__(self, name:str, surname:str, courses:list):
        super().__init__(name, surname)
        self.courses = courses
    
    # Add course to the student
    def addCourse(self, course:Course):
        self.courses.append(course)

class Teacher(Person):
    # Class attribute
    def __init__(self, name:str, surname:str, courses:list, salary:int):
        super().__init__(name, surname)
        self.teaching_in_courses = courses
        self.salary_info = salary
    
    # Add course to the teacher
    def addCourse(self, course:Course):
        self.teaching_in_courses.append(course)
    
    # Print all Courses that the teacher teaches
    def teach(self):
        for course in self.teaching_in_courses:
            print(course.name, end=" ")

calc = Course("Calculus", 3)
algo = Course("Algorithm", 3)
oop = Course("Object Oriented Programming", 3)
ai = Course("Artificial Intelligence", 3)

student1 = Student("Abhipraya", "Abhip", [calc, algo])
student1.addCourse(oop)

teacher1 = Teacher("Fadhlan", "Dlan", [calc, algo], 2500000)
teacher1.addCourse(ai)
teacher1.teach()