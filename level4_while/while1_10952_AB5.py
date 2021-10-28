#사전입출력설정
import sys
input = sys.stdin.readline

# A,B를 저장받을 리스트 생성
ABlist = [1 for i in range(2)]

#입력/처리/출력
i = 0

while i >= 0 :  
  A,B = map(int,input().split()) #입력
  ABlist[0] = A
  ABlist[1] = B

  if ABlist[0] == 0 and ABlist[1] == 0 : #입력후,출력전 탈출조건 명시
   break 

  print(ABlist[0] + ABlist[1]) #출력
  
  i += 1
