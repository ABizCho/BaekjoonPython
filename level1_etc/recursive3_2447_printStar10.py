#입력
inputV = int(input())
k = 0
w = 0
#LV1 ) 입력값 InputV가 3의 몇승인지 판별하여, 그 승값 정수를 k변수에 저장
 ##( k의 도메인으로 사전에 주어진 정수 [1~7]을 반복횟수를 최대 7회까지로 제한하여 3에 제곱하여 저장하기를 반복하며, 매 반복마다 나온 제곱결과를 inputV와 비교하여 같을경우 그 횟수값을 승값인 k값에 저장 )
while w < 7 :
  compV = w+1

  if 3**compV == inputV :
    k = compV
    break
  w += 1

#LV2 ) 승값인 K를 이용해 별찍기 함수에 재귀의 LV이 설정되도록 설계

 #LV2  )

## LV1의 별구조 구현
def printstar1() : 
  i = 0

  while i < 3 :
    j = 0
    print('') #줄바꿈

    while j < 3 :
      if j == 1 & i == 1:
        print(' ',end='')
        j += 1
        continue
      else :
        print('*',end='')
        j += 1

    i += 1

## LVn의 별구조 구현
'''
def printstar2( ) :
  i = 0

  while i < 3 :
    j = 0
    print('') #줄바꿈

    while j < 3 :
      if j == 1 & i == 1 :

        a = 0 
        while a < 3 : 
         print(' ',end='')
         a += 1

        j += 1
        continue
      else :
        printstar1()
        j += 1
    i += 1
'''
###################


printstar1()
#  for i in range(1,10) :
#    print(star)

#printStar33()