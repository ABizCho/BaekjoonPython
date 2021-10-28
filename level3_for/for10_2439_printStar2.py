  #입출력 사전설정
  import sys
  input = sys.stdin.readline

  #입력
  inputV = int(input())

  #기능별 함수 정의

  #공백출력함수 정의
  def space(n) :
    for i in range(n) :
      print(' ',end='')
  #별찍기함수 정의
  def star(n) :
    for i in range(n+1) :
      print('*',end='')

  #처리 및 출력
  for i in range(inputV) :
    space(inputV-(i+1))
    star(i)
    print('')