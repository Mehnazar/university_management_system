# Define the base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

# Define the Student class that inherits from Person
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.courses = []

    def registerForCourses(self, course):
        self.courses.append(course)
        course.addStudent(self)

# Define the Instructor class that inherits from Person
class Instructor(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = []

    def assignCourse(self, course):
        self.courses.append(course)
        course.setInstructor(self)

# Define the Course class
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []
        self.instructor = None

    def addStudent(self, student):
        self.students.append(student)

    def setInstructor(self, instructor):
        self.instructor = instructor

# Define the Department class
class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)

# Example usage
# Create department
cs_department = Department("Computer Science")

# Create courses
course_1 = Course(101, "Data Structures")
course_2 = Course(102, "Algorithms")

# Add courses to the department
cs_department.addCourse(course_1)
cs_department.addCourse(course_2)

# Create students
student_1 = Student("John Doe", 20, "S1001")
student_2 = Student("Jane Smith", 21, "S1002")

# Register students for courses
student_1.registerForCourses(course_1)
student_2.registerForCourses(course_2)

# Create instructors
instructor_1 = Instructor("Dr. Alice", 40, 50000)
instructor_2 = Instructor("Dr. Bob", 45, 55000)

# Assign instructors to courses
instructor_1.assignCourse(course_1)
instructor_2.assignCourse(course_2)

# Output details
print(f"Course: {course_1.name}, Instructor: {course_1.instructor.getName()}, Students: {[student.getName() for student in course_1.students]}")
print(f"Course: {course_2.name}, Instructor: {course_2.instructor.getName()}, Students: {[student.getName() for student in course_2.students]}")
print(f"Department: {cs_department.name}, Courses: {[course.name for course in cs_department.courses]}")
