"""
这是一个模拟猫狗大战的Python程序，通过这个程序可以学习面向对象编程的基本概念，包括类、对象、属性和方法。
1. Cat类（猫类）
类属性：
role = 'cat'：角色标识
实例属性：
name：猫的名字
breed：猫的品种
aggressiveness：攻击力
life_value：生命值
方法：
__init__()：构造函数，初始化猫的属性
attack(dog)：攻击狗的方法，减少狗的生命值
dead_or_alive()：判断猫是否存活

2. Dog类（狗类）
类属性：
role = 'dog'：角色标识
实例属性：
name：狗的名字
breed：狗的品种
aggressiveness：攻击力
life_value：生命值
方法：
__init__()：构造函数，初始化狗的属性
bite(cat)：咬猫的方法，减少猫的生命值
dead_or_alive()：判断狗是否存活
"""


class Cat:
    role = "cat"

    # 初始化猫
    def __init__(self, name, breed, aggressiveness, life_value):
        self.name = name
        self.breed = breed
        self.aggressiveness = aggressiveness
        self.life_value = life_value

    def attack(self, dog):
        dog.life_value = dog.life_value - self.aggressiveness
        print(f"{self.name}猫对{dog.name}狗造成了{self.aggressiveness}点伤害！{dog.name}狗剩余{dog.life_value}点血量。")

    def dead_or_alive(self):
        if self.life_value <= 0:
            print(f"{self.name}猫已经死亡！")
            return False
        return True


class Dog:
    role = "dog"

    # 初始化狗
    def __init__(self, name, breed, aggressiveness, life_value):
        self.name = name
        self.breed = breed
        self.aggressiveness = aggressiveness
        self.life_value = life_value

    def bite(self, cat):
        cat.life_value = cat.life_value - self.aggressiveness
        print(f"{self.name}狗对{cat.name}猫造成了{self.aggressiveness}点伤害！{cat.name}猫剩余{cat.life_value}点血量。")

    def dead_or_alive(self):
        if self.life_value <= 0:
            print(f"{self.name}狗已经死亡！")
            return False
        return True


# 测试代码
cat_1 = Cat("小花", "狸花猫", 15, 100)
dog_1 = Dog("大黄", "哈士奇", 20, 120)
print("------战斗开始-----")
while cat_1.life_value > 0 and dog_1.life_value > 0:
    cat_1.attack(dog_1)
    dog_1.dead_or_alive()
    dog_1.bite(cat_1)
    cat_1.dead_or_alive()
    print("-----------")
print("------战斗结束-----")
