#입출력 사전설정
import sys
input = sys.stdin.readline

#입력 
inputV = int(input())

#처리 및 출력
def star(n) :
  for i in range(n+1) :
    print('*',end='')

for i in range(inputV) :
  star(i)
  print('')
