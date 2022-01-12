## 순차 검색
import random
## 함수
def seqSearch(ary,fData):
    pos = -1
    size = len(ary)
    for i in range(size):
        if (ary[i] == fData):
            pos = i
            break
    return pos

## 전역
SIZE = 10
dataAry = [random.randint(1,99) for _ in range(SIZE)]
findData = dataAry[random.randint(0,SIZE-1)]
# findData = -9

## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1 :
    print(findData, '없어요 ㅠ')
else:
    print(findData, '이', position, '에 있음')
