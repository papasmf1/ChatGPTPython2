class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, skill, title):
        super().__init__(id, name)
        self.skill = skill
        self.title = title

class Employee(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

class Alba(Person):
    def __init__(self, id, name):
        super().__init__(id, name)

# 예시 객체 생성
manager1 = Manager(1, "John", "Leadership", "Senior Manager")
employee1 = Employee(2, "Alice", "Software Engineer")
alba1 = Alba(3, "Bob")

# 객체 정보 출력
manager1.printInfo()
employee1.printInfo()
alba1.printInfo()
