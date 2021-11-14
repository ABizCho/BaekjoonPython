n = int(input())

A = 3
B = 5


# if n % B == 0 :
  
#   print(n//B)
# else :
#   if (n % B) % A == 0 :
#     print((n//B)+((n%B)//A))
    
#   else :
#     if n%A == 0 :
#       print(n//A)
#     else :
#       print(-1)


i = 0
A1=  A
abBreak = True
while 1 :
  B1 = B * i

  
  if B1 == n :
    print(i)
    break
  else :
    for j in range(300):
      A1 = A*j
      if B1+A1 == n:
        abBreak = False
        
        op1 = i+j+2
        break

    if op 1 < i+j+2 :
  i += 1  





