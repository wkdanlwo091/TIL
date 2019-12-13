import random

# greeting = "안녕하세요"

# print(greeting)


# for c in range(1,3):
#     print(greeting)
menus = ['순남', '자강', '두천']
print(menus)
print(menus)

#dictionary 

phone_book = {'순남' : '02-1234-1234', '자강' : '02-1234-1234', '두천' : '02-1234-1234'}
print(phone_book['두천'])

for i in range(0,5):
    print("안녕하세요 어서오세요")

a = 20
while(a >10):
    print("안녕히가세요")
    a = a-1

a = 200
while True:
    if(a> 150):
        print("매우나쁨")
    elif(a <= 150 or a > 80):
        print("나쁨")
    elif(a <= 80 or a > 30):
        print("보통")
    else :
        print("좋음")
    break


list = []
for i in range(1, 46):
    list.append(i)

lotto_num = random.sample(list, 6)
print(lotto_num)

numbers = random.sample(range(1,46), 6)
print(numbers)