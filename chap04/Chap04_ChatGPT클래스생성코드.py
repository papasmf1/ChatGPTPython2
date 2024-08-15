#Chap04_ChatGPT클래스생성코드.py 
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

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Alba(Person):
    def __init__(self, id, name):
        super().__init__(id, name)

    def printInfo(self):
        super().printInfo()

# 인스턴스 생성 및 출력
instances = [
    Manager(1, "Alice Johnson", "Management", "General Manager"),
    Manager(2, "Bob Smith", "IT", "IT Manager"),
    Employee(3, "Charlie Brown", "Software Engineer"),
    Employee(4, "David Wilson", "Analyst"),
    Alba(5, "Eve Davis"),
    Alba(6, "Frank Miller"),
    Manager(7, "Grace Lee", "Marketing", "Marketing Manager"),
    Employee(8, "Hannah Martin", "HR Specialist"),
    Alba(9, "Ivy Thompson"),
    Employee(10, "Jack White", "Sales Representative")
]

for instance in instances:
    instance.printInfo()
    print()
