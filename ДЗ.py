class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_gr(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        val = list(self.grades.values())
        if len(val) > 0:
           return sum(*val) / len(*val)
        else:
            return 0

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания:{self.average_grades()}
Курсы в процессе изучения:{self.courses_in_progress}
Завершенные курсы:{self.finished_courses}"""

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grades() < other.average_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        val = list(self.grades.values())
        if len(val) > 0:
           return sum(*val) / len(*val)
        else:
            return 0

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции:{self.average_grades()}"""

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_grades() < other.average_grades()

class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['C++']

best_student2 = Student('Sasha', 'Pop', 'your_gender')
best_student2.courses_in_progress += ['Python']

cool_mentor = Lecturer('Bob', 'Stiv', 'Python')
cool_mentor.courses_attached += ['Python']

cool_mentor2 = Lecturer('Misha', 'Rysev', 'Python')
cool_mentor2.courses_attached += ['Python']

cool_reviewer = Reviewer('Jon', 'Smit', 'Python')
cool_reviewer.courses_attached += ['Python']

#Студент ставит оценку преподавателю
best_student.rate_gr(cool_mentor, 'Python', 10)
best_student.rate_gr(cool_mentor, 'Python', 10)

best_student2.rate_gr(cool_mentor2, 'Python', 8)
best_student2.rate_gr(cool_mentor2, 'Python', 8)

#Проверяющий ставит оценку студенту
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 4)

cool_reviewer.rate_hw(best_student2, 'Python', 5)
cool_reviewer.rate_hw(best_student2, 'Python', 3)

print(cool_reviewer) #Задание 3.1
print('_______________________________________________________')
print(cool_mentor) #Задание 3.2
print('_______________________________________________________')
print(best_student) #Задание 3.3
print('_______________________________________________________')

print(f'Результат сравнения студентов(по средним оценкам за ДЗ): '
      f'{best_student.name} {best_student.surname} < {best_student2.name} {best_student2.surname} = {best_student > best_student2}')
print('_______________________________________________________')

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{cool_mentor.name} {cool_mentor.surname} < {cool_mentor2.name} {cool_mentor2.surname} = {cool_mentor > cool_mentor2}')
print('_______________________________________________________')

#Задание 4
student_list = [best_student, best_student2]
lecturer_list = [cool_mentor, cool_mentor2]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_grades()
            count_all += 1
    return sum_all / count_all

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_grades()
            count_all += 1
    return sum_all / count_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print('_______________________________________________________')

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print('_______________________________________________________')