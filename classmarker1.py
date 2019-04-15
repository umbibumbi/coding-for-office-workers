# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
import random
food = input("한식, 중식, 일식 중 한 가지를 고르세요 : ")

if food == "한식":
    list_korean = ["떡볶이", "감자탕", "등갈비", "평양냉면"]
    food_result = random.choice(list_korean)
    # food_result = list_korean(random.randint(0, len(list_korean)))

elif food == "중식":
    list_chinese = ["양장피", "깐풍기", "오렌지치킨", "쟁반짜장"]
    food_result = random.choice(list_chinese)

elif food == "일식":
    list_japanese = ["오마카세스시", "가츠동", "자루소바", "몬자야끼"]
    food_result = random.choice(list_japanese)

else :
    print("한식, 중식, 일식만 가능합니다")

if food_result:
    print("{} 중에서 {}(이/가) 선택되었습니다. ".format(food, food_result))
