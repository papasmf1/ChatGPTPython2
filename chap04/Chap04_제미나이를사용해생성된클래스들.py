class Person:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def printInfo(self):
    print(f"아이디: {self.id}")
    print(f"이름: {self.name}")

class Manager(Person):
  def __init__(self, id, name, skill, title):
    super().__init__(id, name)  # 부모 클래스 생성자 호출
    self.skill = skill
    self.title = title

  def addSkill(self, new_skill):
    self.skill.append(new_skill)

class Employee(Person):
  def __init__(self, id, name, title):
    super().__init__(id, name)  # 부모 클래스 생성자 호출
    self.title = title

# 객체 생성 및 테스트
p = Person(1001, "철수")
p.printInfo()

m = Manager(1002, "영희", ["개발", "설계"], "팀장")
m.printInfo()
print(f"직책: {m.title}")
m.addSkill("데이터 분석")
print(f"추가된 기술: {m.skill}")

e = Employee(1003, "민수", "사원")
e.printInfo()
print(f"직책: {e.title}")
