"""
动物园管理系统

请完成以下任务：
1. 创建 Bird 类继承 Animal 类
    - 添加特有属性：wing_span（翼展）
    - 重写 make_sound 方法，返回"叽叽喳喳"
    - 重写 move 方法，返回"飞行"

2. 创建 Dog 类继承 Animal 类
    - 添加特有属性：breed（品种）
    - 重写 make_sound 方法，返回"汪汪汪"
    - 重写 move 方法，返回"跑步"

3. 创建 Zoo 类
    - 实现 add_animal 方法，添加动物到动物园
    - 实现 make_all_sounds 方法，让所有动物发出声音
    - 实现 show_all_animals 方法，展示所有动物的信息

预期输出：
叽叽喳喳
汪汪汪
小鸟：我是小鸟，今年2岁，翼展0.3米，移动方式：飞行
旺财：我是旺财，今年3岁，品种：哈士奇，移动方式：跑步
"""


class Animal:
    """动物基类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        """发出声音"""
        return "sound"

    def move(self):
        """移动方式"""
        return "动物在移动"

    def introduce(self):
        """自我介绍"""
        return f"我是{self.name}，今年{self.age}岁"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "叽叽喳喳"

    def move(self):
        return "飞行"

    def introduce(self):
        return f"{self.name}：{super().introduce()}，翼展{self.wing_span}米，移动方式：{self.move()}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "汪汪汪"

    def move(self):
        return "跑步"

    def introduce(self):
        return f"{self.name}：{super().introduce()}，品种：{self.breed}，移动方式：{self.move()}"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def make_all_sounds(self):
        for ani in self.animals:
            print(ani.make_sound())

    def show_all_animals(self):
        for ani in self.animals:
            print(ani.introduce())


# 测试代码
zoo = Zoo()
bird = Bird("小鸟", 2, 0.3)
dog = Dog("旺财", 3, "哈士奇")
zoo.add_animal(bird)
zoo.add_animal(dog)

zoo.make_all_sounds()
zoo.show_all_animals()


"""
学生管理系统示例
请完成以下任务：
1. 创建 Student 类
    - 类属性 total_students，记录学生总数
    - 实例属性 name（姓名）、score（分数）
    - 构造函数中每创建一个实例，total_students 增加1
    - 类方法 get_total，返回当前学生总数
    - 静态方法 check_score，验证分数是否合法（0-100之间）
"""


class Student:
    total_students = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score

        Student.total_students += 1

    @classmethod
    def get_total(cls):
        return cls.total_students

    @staticmethod
    def check_score(score):
        if 0 <= score <= 100:
            return True
        return False


# 创建学生
s1 = Student("张三", 85)
s2 = Student("李四", 90)

# 获取学生总数
print(f"学生总数: {Student.get_total()}")  # 预期输出：学生总数: 2

# 检查分数
print(f"95分是否合法: {Student.check_score(95)}")  # 预期输出：True
print(f"150分是否合法: {Student.check_score(150)}")  # 预期输出：False
