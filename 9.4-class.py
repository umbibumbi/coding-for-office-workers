
class FourCal:
    def __init__(self, first, second):   # ① 메서드의 매개변수
        self.first = first              # ② 메서드의 수행문
        self.second = second            # ② 메서드의 수행문
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def min(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# a = FourCal(15, 0)
# print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal(5, 4)
print(b.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

c = SafeFourCal(5, 0)
print(c.div())
