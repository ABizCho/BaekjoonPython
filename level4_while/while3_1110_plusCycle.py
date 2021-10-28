#입출력 사전설정
import sys
input = sys.stdin.readline

#입력
N = int(input())

#사이클 부품 준비
n = -1  #사이클 내에서 종료판별기준 N과 비교될 값 n을 선언
A = N // 10 # 두자리 수 N중 첫번째 자리를 A에 저장
B = N % 10  # 두라지 수 N중 마지막 자리를 B에 저장
cycleLength = 0

#처리 및 출력
while cycleLength >= 0 :
  if n == N :
    break
  
  sumV = A + B
  sumV = sumV % 10 

  n = B*10 + sumV

  A = n // 10 
  B = n % 10
  
  cycleLength += 1


print(cycleLength)

  
