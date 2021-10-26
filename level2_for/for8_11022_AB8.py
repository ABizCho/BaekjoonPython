#
import sys
input = sys.stdin.readline

#테스트횟수 입력
inputT = int(input())

#2차원리스트(AB저장공간) 생성
ABlist = [[0 for i in range(2)] for i in range(inputT)]

#테스트케이스 입력/처리/출력

for i in range( inputT ) :
  ABlist[i][0],ABlist[i][1] = map(int,input().split())
  
  print("Case #{0}: {1} + {2} = {3}".format(i+1, ABlist[i][0], ABlist[i][1], ABlist[i][0] + ABlist[i][1]))