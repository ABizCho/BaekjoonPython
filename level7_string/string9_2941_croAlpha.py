a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alpha = input()

print(alpha)

for t in a :
  alpha = alpha.replace(t,'*')
  
print(len(alpha))