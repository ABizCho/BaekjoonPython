#사전입출력설정
import sys
input = sys.stdin.readline

#입력
intInput = []
for i in range(3) :
  intInput.append(int(input()))

#처리 및 출력

  #(1) 곱셈저장
mulResult = intInput[0]*intInput[1]*intInput[2]
  #(2) 결과값이 몇의자리 수인지 판별
    # + 실시간 판별하며 각자리값 리스트에 저장
valList = []
tempDigit = mulResult
i = 0

while 1 : 
  valList.append(tempDigit % 10)#한자리수부터 순서대로 저장
  tempDigit = tempDigit // 10 #총 자릿수판별
  i += 1  

  if tempDigit == 0 : #종료조건
    break

  #(3) count의 기준이 될 비교 리스트에 0~9 저장
numList= []
numList.extend(map(int,range(10)))

  #(4) valList와 numList 0~9까지 비교 및 count 순차출력 
count = 0
for i in numList :
  for j in valList :
    if j == i :
      count += 1
  print(count)
  count = 0