# my_dict = {'한국어':'안녕', '영어':'hi', '독일어':'Guten tag'}

# my_dict2 = {}
# my_dict2['한국어'] = '안녕'
# my_dict2['영어'] = 'hi'
# my_dict2['독일어'] = 'Guten tag'

# my_dict3 = dict(한국어='안녕', 영어 = 'hi' , 독일어 = 'Guten tag')

# print(my_dict)
# print(my_dict2)
# print(my_dict3)

area_code = {'서울': '02'}
# area_code['경기도'] = '031'
# print(area_code)

# for key in area_code:
#     print(key)##key 값
#     print(area_code[key])##value 값
    
# for key, value in area_code.items():
#     print(key, value)

for value in area_code.values():
    print(value)

for value in area_code.keys():
     print(value)

'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
sum = 0 
for value in score.values():
    sum = sum + value
print(sum/len(score))
# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 84,
        '국어': 90,
        '음악': 92
    },
    'b': {
        '수학': 83,
        '국어': 91,
        '음악': 77
    }
}
total = 0
for key, value in scores.items():
    sum = 0
    for valueOfvalue in value.values():
        sum = sum + valueOfvalue
    print(key + "의 평균")
    print(sum/len(value))
    total = total + sum/len(value)
total = total/len(scores)
print('반의 평균은 ' , total)

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

for key, value in city.items():
    sum = 0
    for valueOfvalue in value:
        sum = sum + valueOfvalue
    print(key , '의 최근 3일 평균 온도는 ' ,  sum/len(value))

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cityMax = -100
cityMin = 100
coldest = 0 
hottest =  0
for key, value in city.items():
    for valueOfvalue in value:
        print(valueOfvalue)
        if( cityMax < valueOfvalue):
            cityMax = valueOfvalue
            hottest = key
        if( cityMin > valueOfvalue):
            cityMin = valueOfvalue
            coldest = key
print('가장 추운 곳 ', coldest)
print('가장 더운 곳', hottest)


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
key = '서울'
if key in city:
    print("dictionary에 서울이 있습니다. ")
    for value in city[key]:
        if(value == 2):
            print("네")
            break
    print("서울은 영상 2도였던 적이 없습니다. ")
    
# for key, value in city.items():
#     print(key)
#     if(key == "서울"):
#         for valueOfvalue in value:
#             if(valueOfvalue == 2):
#                 print("yes")
#     elif(key != '서울'):
#         print("no")
#         break
# 아래에 코드를 작성해 주세요.
