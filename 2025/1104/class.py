class Student:

    # 私有变量 __

    __school_name = "延边大学"
    __total_students = 0

    # 初始化函数
    def __init__(self, name, age, id_card):
        self.name = name
        self.age = age
        self.courses = []

        self.__id_card = id_card
        self.__grades = {}

        self.student_id = None  # 学号
        Student.__total_students += 1
        self.student_id = f"{Student.__total_students:3d}"

    # 选课行为
    def enroll_course(self, course_name):
        self.courses.append(course_name)
        return f"{self.name}选修了{course_name}"

    # 显示学校
    def show_school_name(self):
        return self.__school_name

    # 成绩录入
    def record_grade(self, course_name, grade):
        if course_name in self.courses:
            if 0 <= grade <= 100:
                self.__grades[course_name] = grade
                return f"{course_name}成绩为{grade}"
            else:
                return "成绩必须在0-100之间"
        else:
            return "未选择该课程"

    # 显示成绩
    def get_grade(self, course_name):
        if course_name in self.__grades:
            return self.__grades[course_name]
        else:
            return "未记录该课程成绩"


student1 = Student("张三", 18, "11010101010101010")

print(Student.show_school_name(student1))

student1.enroll_course("Python")
student1.record_grade("Python", 100)
print(student1.get_grade("Python"))
