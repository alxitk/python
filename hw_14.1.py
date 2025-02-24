# HW 14.1. Група студентів
class GroupLimitError(Exception):
    pass
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"


class Group:
    MAX_NUMBER_OF_STUDENTS = 10
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_NUMBER_OF_STUDENTS:
            raise GroupLimitError(f"Too much students in this group")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for i in self.group:
            if i.last_name == last_name:
                return i
        return None

    def __str__(self):
        all_students = "\n".join(str(i) for i in self.group)
        return f"Number:{self.number}\n{all_students}"




st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
st3 = Student("Male", 25, "David", "Beckham", "AN145")
st4 = Student("Male", 25, "Roy", "Keane", "AN145")
st5 = Student("Male", 25, "Andy", "Cole", "AN145")
st6 = Student("Male", 25, "Dwight", "Yorke", "AN145")
st7 = Student("Male", 25, "Paul", "Scholes", "AN145")
st8 = Student("Male", 25, "Gary", "Neville", "AN145")
st9 = Student("Male", 25, "Denis", "Irwin", "AN145")
st10 = Student("Male", 25, "Phil", "Neville", "AN145")
st11 = Student("Male", 25, "Alex", "Ferguson", "AN145")

gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
# gr.add_student(st11)
print(gr)

