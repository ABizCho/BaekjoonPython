n = 0
while n < 3 :
  #입력
  H, M = map(int,input().split())

  #처리및출력
  if M >= 45 :
    M - 45
  elif M < 45 :
    residual = 45 - M
    M = 60-residual
    H -= 1
    if H < 0 :
      H = 23

  print(H,M)
  n += 1
