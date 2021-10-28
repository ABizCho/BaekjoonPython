
#입력
H, M = map(int,input().split())

#테스트입력
#i = 0

#for i in range(12) :
#H = 1
#M = i*5
#print('입력',H,M)

#처리및출력
if M >= 45 :
  M = M - 45
elif M < 45 :
  residual = 45 - M
  M = 60-residual
  H -= 1
  if H < 0 :
    H = 23

print(H,M,'\n')

