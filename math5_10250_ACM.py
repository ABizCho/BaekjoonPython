T = int(input())

for i in range(T):
  h,w,n = map(int,input().split())
  
  if n % h == 0 :
    x = h
    y = n//h 
  else : 
    x = n % h
    y = n // h + 1


  if y < 10 :
    print('{0}0{1}'.format(x,y))
  else :
    print('{0}{1}'.format(x,y))
    
  if 