#입출력 사전설정
import sys 
input = sys.stdin.readline

#1차원 리스트 생성
ABlist = [1 for i in range(2)]

#입력/처리/출력
i = 0 
while i >= 0 :
  try : 
    ABlist[0],ABlist[1] = map(int,input().split()) 
    print(ABlist[0]+ABlist[1])
  except : 
    break