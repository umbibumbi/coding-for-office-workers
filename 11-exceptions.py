# exceptions 예외

# ZeroDivisionError
# 1 / 0
def divide_by(first, second):
    try:
        return first / second
    except ZeroDivisionError :
        return "0으로 나눌 수 없습니다"

print(int(divide_by(4, 2)))
print(divide_by(4, 0))

# 예외 만들기 exceptions
class EvenNumberDivisionError(Exception):
    pass
#Class 이름 정할 때는 CamelCase
#그 외의 함수, 변수 이름 정할 때는 _ 사용
def divided_by_odd_number(first, second):
    if second % 2 == 0 :
        raise EvenNumberDivisionError
    else:
        return first / second
print(divided_by_odd_number(6, 3))
print(divided_by_odd_number(6, 2))
