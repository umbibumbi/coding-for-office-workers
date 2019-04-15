#사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
#직장 동료 클래스를 사람 클래스를 이용해서 만듭시다. 사람 기본 요소 외 별도의 추가 사항은 직급입니다.

# 클래스/상속
# 사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들 때, 입력을 받을 수 있도록 합시다.
# 직장 동료의 기본 직급은 "대리"로 지정합니다.
# (고급) 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서, 직급도 처음 만들어질 때 입력하도록 변경을 도전해봅시다.



class Saram():
    def __init__(self, name, age, gender):
        self.first = name
        self.second = age
        self.last = gender

class Col(Saram):
    position = "대리"


a = Saram("Eunbi", "30세", "여자")
print(a.first)

b = Col("Nori", "41세", "남자")
print(b.position)
print(b.last)





















# class People:
#     name = ""
#     age = ""
#     gemder = ""
#
#     def __init__(self, age, gender):
#         self.age = age
#         self.gender = gender
#
# person1 = People("30세", "여성")
# print(person1.gender)
# print(person1.age)
#
#
# class WorkPeople(People):
#     position = "대리"
#
#
# # person2 = WorkPeople("","")
# # print(person2.position)
# # person2.age = "43세"
# # print(person2.name)
