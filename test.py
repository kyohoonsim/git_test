class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(f'제 이름은 {self.name}입니다.')
    
    def get_age(self):
        print(f'제 나이는 {self.age}세 입니다.')


class Student(Person):
    def __init__(self, name, age, GPA):
        super().__init__(name, age)
        self.GPA = GPA

    def get_GPA(self):
        print(f'제 학점은 {self.GPA}입니다.')


class Student(Person):
    def __init__(self, name, age, GPA):
        super().__init__(name, age)
        self.GPA = GPA

    def get_GPA(self):
        print(f'제 학점은 {self.GPA}입니다.')


student_a = Student('김OO', 27, 3.4)
student_a.get_name()
student_a.get_age()
student_a.get_GPA()


class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, self.power)

class Monster(Unit):
    def __init__(self, name, power, type):
        super().__init__(name, power)
        self.type = type
    def show_info(self):
        print(self.name, self.type)

monster = Monster('슬라임', 10, '초급')
monster.show_info()
monster.attack()