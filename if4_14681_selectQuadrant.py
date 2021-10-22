#사전설정
quad = [ 1, 2, 3, 4 ]

#입력
x = int(input())
y = int(input())

#처리 및 출력
if x > 0 :
  if y > 0 :
    print(quad[0])
  elif y < 0 :
    print(quad[3])
elif x < 0 :
  if y > 0 :
    print(quad[1])
  elif y < 0 :
    print(quad[2])