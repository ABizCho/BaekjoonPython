x = int(input())
line = 1

while x > line :
  x -= line 
  line += 1 
  print('x:',x,'line:',line)

if line % 2 == 0 :
  
  print('{0}/{1}'.format(x,line-x+1))
else :
  print('{0}/{1}'.format(line-x+1,x))