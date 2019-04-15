dan = int(input("몇 단을 출력하시겠습니까"))
if dan > 0 and dan < 10:
    for num in range (1, 10):
        print("{} * {} = {}".format(dan, num, dan * num))
else:
    print("1부터 9까지의 숫자를 넣어주세요")
