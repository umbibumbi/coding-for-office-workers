# 함수 functions
# 입력값 parameters 반환값 returns

def hello_friends(name):
    print("hello, {}".format(name))
name1 = "EUNBI"
name2 = "KINAM"

hello_friends(name1)
hello_friends(name2)

# 반환값 = return : 변수에 대입해 쓸 수 있다.

# # 입력값 o, 반환값 o
def sum(a, b) #입력값
    return a + b #반환값
# # 입력값 o, 반환값 x
def hello_friends(name):
    print("hello, {}".format(name))
# # 입력값 x, 반환값 o
def return_1():
    return 1
num_1 = return_1() #변수에 대입해 쓰는 예시
print(num_1)
# # 입력값 x, 반환값 x
def hello_world():
    print("hello world")
