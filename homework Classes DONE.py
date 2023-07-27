class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def list_to_str_progress(self):
        ready_str_progress = ''.join(self.courses_in_progress)
        return ready_str_progress

    def list_to_str_finish(self):
        ready_str_finish = ''.join(self.finished_courses)
        return ready_str_finish

    def rate_cw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_grades(self):
        for grade in self.grades:
            avg_grades = sum(self.grades[grade]) / len(self.grades[grade])
            return avg_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._avg_grades()}' \
              f'\nКурсы в процессе обучения: {self.list_to_str_progress()}' \
              f'\nЗавершенные курсы: {self.list_to_str_finish()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются не студенты!')
            return
        return self._avg_grades() < other._avg_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def _avg_grades(self):
        for grade in self.grades:
            avg_grades = sum(self.grades[grade]) / len(self.grades[grade])
            return avg_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_grades()} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются не лекторы!')
            return
        return self._avg_grades() < other._avg_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def avg_grade_course_stud(students, course):
    sum_grade = 0
    count = 0
    for student in students:
        if isinstance(student, Student):
            if course in student.grades:
                for el in student.grades[course]:
                    sum_grade = sum_grade + el
                    count += 1
        else:
            print('Это не студент!')
    if count == 0:
        print('У студентов нет оценок по данному курсу')
    else:
        print(sum_grade/count)


def avg_grade_course_lec(lecturers, course):
    sum_grade = 0
    count = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                for el in lecturer.grades[course]:
                    sum_grade = sum_grade + el
                    count += 1
        else:
            print('Это не лектор!')
    if count == 0:
        print('Лекторы не имеют оценок по данному курсу')
    else:
        print(sum_grade/count)


def avg_for_all(objects, course):
    sum_grade = 0
    count = 0
    for obj in objects:
        if isinstance(obj, Student):
            if course in obj.grades:
                for el in obj.grades[course]:
                    sum_grade = sum_grade + el
                    count += 1
        elif isinstance(obj, Lecturer):
            if course in obj.grades:
                for el in obj.grades[course]:
                    sum_grade = sum_grade + el
                    count += 1
    if count == 0:
        print('Нет оценок по данному курсу!')
    else:
        print(sum_grade / count)

student_list = []
lecturer_list = []

first_student = Student('Tony', 'Montana', 'male')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Java']
first_student.finished_courses += ['C#']
student_list.append(first_student)

secod_student = Student('Bruce', 'Kotov', 'male')
secod_student.courses_in_progress += ['C#', 'Python']
secod_student.finished_courses += ['Java']
student_list.append(secod_student)

first_lecturer = Lecturer('Eddard', 'Stark')
first_lecturer.courses_attached += ['Java']
lecturer_list.append(first_lecturer)

second_lecturer = Lecturer('John', 'Snow')
second_lecturer.courses_attached += ['Java']
lecturer_list.append(second_lecturer)

first_reviewer = Reviewer('Tom', 'Readle')
first_reviewer.courses_attached += ['Python', 'C#', 'Java']

second_reviewer = Reviewer('Janna', 'Aguzarova')
second_reviewer.courses_attached += ['Java']


first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(secod_student, 'C#', 6)
first_reviewer.rate_hw(secod_student, 'C#', 7)
first_reviewer.rate_hw(secod_student, 'Python', 9)
first_reviewer.rate_hw(secod_student, 'Python', 10)
first_student.rate_cw(first_lecturer, 'Java', 10)
first_student.rate_cw(first_lecturer, 'Java', 8)
first_student.rate_cw(first_lecturer, 'Java', 9)
first_student.rate_cw(second_lecturer, 'Java', 9.5)
first_student.rate_cw(second_lecturer, 'Java', 10)
first_student.rate_cw(second_lecturer, 'Java', 9)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(first_student.grades)
# print(second_student.grades)
# print(first_lecturer.grades)
print(first_lecturer)
print(first_student)
print(second_lecturer)
print(second_lecturer.__lt__(first_lecturer))
print(first_student.__lt__(secod_student))
# print(first_student.__lt__(first_lecturer))
#
# print(student_list)
# print(lecturer_list)

avg_grade_course_stud(student_list, 'Python')
avg_grade_course_lec(lecturer_list, 'Java')

avg_for_all(student_list, 'Python')
avg_for_all(lecturer_list, 'Java')