#입출력 사전설정
import sys
input = sys.stdin.readline

inputT = int(input())

#입력받을 ' 2 x n ' 2차원리스트 생성
ABlist = [[0 for j in range(2)] for i in range(inputT)]

#입력
for i in range (inputT) :
  ABlist[i][0] , ABlist[i][1] = map(int,input().split())

  print(ABlist[i][0] + ABlist[i][1])


