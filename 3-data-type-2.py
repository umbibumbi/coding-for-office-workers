# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

#
# # list [ ]
# print("list")
# list_a = [1, 2, 3]
# # print(list_a)
# # index는 0부터 시작
# # print(list_a[0])
# # print(list_a[1])
# # #slice /
# print(list_a[0:2]) #:이후의 index는 포함되지 않음
# list_a.append(4) #add item
# print(list_a)
# list_a.remove(3) #remove item
# print(list_a)
# list_a.clear() #remove everything


#tuple (1, ) tuple은 변경이 안됨 (내용의 안정성 보장)
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type((tuple_a)))

# dictionary {} (다른 언어에서는 map)
# key & value 로 구성
# dict_a = {
#  "apple" : "a type of fruits",
#  "pen" : "a thing to write"
#  } #{ key : value}
# print(dict_a)
# dict_a["pen"] = "something to write"
# print(dict_a)
#
# #set ([]) 집합 / 중복 자동 제거
# set_a = set([1, 2, 3, 3, 2])
# set_b = set([2, 4, 6])
# print(set_a)
# print(set_b)
#
# print(set_a & set_b) #교집합
# print(set_a | set_b) #합집합
# print(set_a - set_b) #차집합
