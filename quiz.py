# user_input = input("숫자를 입력하세요")
# numbers = user_input.split(",")
# total = 0
# for i in numbers:
#     total += int(i)
# print(total)


# # writedata.py
# f = open("C:/doit/새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(61)
print(cal.value)
