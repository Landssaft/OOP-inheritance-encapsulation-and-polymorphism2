class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
        def str(self):
            ever_grade = average_mark_student
            return f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.ever_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
            
        def rate_hw(self, Lecturer, course, grade):
            if isinstance(lecturer,
                          Lecturer) and course in self.courses_attached and course in lecturer.self.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'


class student_number1(Student):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
        def str(self):
            ever_grade = average_mark_student
            return f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.ever_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'

        def rate_hw(self, Lecturer, course, grade):
            if isinstance(lecturer,
                          Lecturer) and course in self.courses_attached and course in lecturer.self.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'


class student_number2(Student):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
        def str(self):
            ever_grade = average_mark_student
            return f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.ever_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'

        def rate_hw(self, Lecturer, course, grade):
            if isinstance(lecturer,
                          Lecturer) and course in self.courses_attached and course in lecturer.self.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        
        def str(self):
            ever_grade_lecturer = average_mark_lecturer
            return f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.ever_grade_lecturer()}\n'


class lecturer_number1(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        
        def str(self):
            ever_grade_lecturer = average_mark_lecturer
            return f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.ever_grade_lecturer()}\n'


class lecturer_number2(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        
        def str(self):
            ever_grade_lecturer = average_mark_lecturer
            return f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.ever_grade_lecturer()}\n'
            
            
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        def str(self):
            ever_grade = average_mark_student
            return f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'

        def rate_hw(self, student, course, grade):
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
            
            
def average_mark_student(student_list, course_name):
    summary = 0
    student: Student
    for student in student_list:
        for course in student.grades.keys():
            if course != course_name:
                pass
            else:
                summary += student.grades.values()
                result = summary / len(student_list)
                return result
print(average_mark_student)
student_list = [student_number1, student_number2]


def average_mark_lecturer(lecturer_list, course_name):
    summary = 0
    lecturer: lecturer
    for lecturer in lecturer_list:
        for course in lecturer.grades.keys():
            if course != course_name:
                pass
            else:
                summary += lecturer.grades.values()
                result = summary / len(lecturer_list)
                return result
                
lecturer_list = [lecturer_number1, lecturer_number2]

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)