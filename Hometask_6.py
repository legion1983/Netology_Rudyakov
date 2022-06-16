class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        printing = f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за лекцию: {self.avarage_mark()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return printing


    def avarage_mark(self):
        values_summ = 0
        for values in self.grades.values():
            values_number = len(values)
        for values in self.grades.values():
            for marks in values:
                values_summ += marks

        avarage_mark = values_summ / values_number
        return avarage_mark

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.avarage_mark() < other.avarage_mark()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __str__(self):
        printing = f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за лекцию: {self.avarage_mark()}'
        return printing

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def avarage_mark(self):
        values_summ = 0
        for values in self.grades.values():
            values_number = len(values)
        for values in self.grades.values():
            for marks in values:
                values_summ += marks

        avarage_mark = values_summ / values_number
        return avarage_mark

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a student')
            return
        return self.avarage_mark() < other.avarage_mark()

class Reviewer(Mentor):
    pass

    def __str__(self):
        printing = f'Имя: {self.name}\nФамилия:{self.surname}'
        return printing

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

#student N1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'GIT']
best_student.finished_courses += ['Введение в программирование']

#student N2
best_student_2 = Student('Darya', 'Rusakova', 'your_gender')
best_student_2.courses_in_progress += ['Python', 'Mathcad']
best_student_2.finished_courses += ['Введение в программирование']

#cool_reviewer N1
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

#student N1
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 8)
print(best_student.grades)
print('')

#student N2
cool_reviewer.rate_hw(best_student_2, 'Python', 9)
cool_reviewer.rate_hw(best_student_2, 'Python', 9)
print(best_student_2.grades)
print('')

#lecturer N1
best_lecturer = Lecturer('Pavel', 'Rudyakov')
best_lecturer.courses_attached += ['Python']

best_student.rate_hw(best_lecturer, 'Python', 7)
best_student.rate_hw(best_lecturer, 'Python', 8)

#lecturer N2
best_lecturer_2 = Lecturer('Oleg', 'Davydov')
best_lecturer_2.courses_attached += ['Python']

best_student.rate_hw(best_lecturer_2, 'Python', 1)
best_student.rate_hw(best_lecturer_2, 'Python', 2)

print(best_lecturer.grades)
print(cool_reviewer)
print('')
print(best_lecturer)
print('')
print(best_student)
print(best_student_2)
print('')
print(f'Сравнение двух студентов по оценкам, что у 1го оценки хуже чем у 2го, Оценка средняя 1го: {best_student.avarage_mark()}, Оценка средняя 2го: {best_student_2.avarage_mark()}, {best_student < best_student_2}')

print(f'Сравнение двух лекторов по оценкам, что у 1го оценки хуже чем у 2го, Оценка средняя 1го: {best_lecturer.avarage_mark()}, Оценка средняя 2го: {best_lecturer_2.avarage_mark()}, {best_lecturer < best_lecturer_2}')

#Функции для задания 4

def students_avr_result(students_list, course):
#средние оценки студентов на курсе
    sum = 0
    student_q_ty = len(students_list)
    for students in students_list:
        if isinstance(students, Student) and course in students.courses_in_progress:
            for values in students.grades[course]:
                sum += values
    avarage = sum/student_q_ty
    print(f'Средняя оценка студентов по курсу {course}, равна: {avarage} баллов')


def lecturers_avr_result(lecturers_list, course):
#средние оценки лекторов на курсе
    sum = 0
    lecturers_q_ty = len(lecturers_list)
    for lecturers in lecturers_list:
        if isinstance(lecturers, Lecturer) and course in lecturers.courses_attached:
            for values in lecturers.grades[course]:
                sum += values
    avarage = sum/lecturers_q_ty
    print(f'Средняя оценка лекторов по курсу {course}, равна: {avarage} баллов')

#Выводы значений
students_avr_result(students_list=[best_student, best_student_2], course='Python')
print('')
lecturers_avr_result(lecturers_list=[best_lecturer, best_lecturer_2], course='Python')