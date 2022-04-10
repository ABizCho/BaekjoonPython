# 파이썬 비트마스크 : https://justkode.kr/algorithm/bitmash
S = 0b0

def bitmask(
    op, n) :
    global S
    if op == 'add':
        S |= (1 << n)
    
    elif op == 'remove':
        S &=  ~(1 << n)
    elif op == 'check' :
        if S & (1 << n) == 0 :
            print(0)
        else :
            print(1)
    elif op == 'toggle' :
        S ^= (1 << n)
    elif op == 'all' :
        S = 0b11111111111111111111
    elif op == 'empty': 
        S = 0b0

M = int(input()) 
  
for i in range(M):
  op,n = input().split(' ')
  n = int(n)
  

  bitmask(op,n)

 
