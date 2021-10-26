# 입력
#A, B = input().split() #1회시도 틀림
A, B = map(int,input().split()) #2회시도 정답

# 처리및 출력

if A > B :
  print('>')
elif A < B :
  print('<')
else :
  print("==")



