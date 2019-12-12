import requests 
import random

# 888회 로또번호 가져오기

# 그 중에서 번호 6개만 가져오기

# 랜덤으로 로또번호 생성하기

# 실제 당첨번호와 랜덤으로 생성한 로또번호의 
# 일치하는 정도에 따른 등수 표시하기


URL_GetLottoNumber = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" # 현재 동행로또 주소
 
sDrwNum = input("당첨번호를 확인할 회차 번호를 입력해주세요 : ")
resp = requests.get(URL_GetLottoNumber + sDrwNum)

jsResult = resp.json()
 
if jsResult["returnValue"] == "success":
    print(jsResult)
else:
    print("존재하지 않는 회차 번호입니다. (입력됨 : %s)" % (sDrwNum))


mystr = 0
lottoNum =""
lottoList = []
for i in range(1,7):
    temp = 'drwtNo' + str(i)
    print(temp)
    lottoList.append(jsResult[temp])
    lottoNum += str(jsResult[temp])
print(sDrwNum,"의 로또 번호는 " ,lottoNum)
print(sDrwNum, "의 로또 리스트는", lottoList)

predictLotto = ''
predictList = []
for i in range(1,7):
    num = random.randint(1, 45)
    predictLotto +=str(num)
    predictList.append(num)
# 2* 6 
print("당신의 예측은", predictLotto)
print("당신의 로또 리스트는 ", predictList)

cnt = 0
for index, number in enumerate(predictList, start = 0):
    print(index)
    if(number == lottoList[index] ):
        cnt += 1
print("일차하는 숫자의 갯수는 ?", cnt)

cnt = 0

numbers = predictList
winner = lottoList

matched = 0
while matched <6:
    matched = 0
    numbers = sorted(random.sample(range(1,46), 6))
    for num in numbers:
        if num in winner:
            matched += 1
    if(matched == 6):
        print("1등입니다.")
        break
    elif(matched == 5):
        print("2등")
    elif(matched == 4):
        print("3등")
    elif(matched == 3):
        print("4등")
    cnt +=1
print(cnt)