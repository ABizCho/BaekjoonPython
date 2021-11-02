numList = list()
numList.extend(list( map( list, input().split(' '))))

for i in range(len(numList)) :
  numList[i] = list(reversed(numList[i]))

a = str()
for i in range(len(numList[0])) :
  a += numList[0][i]
int(a)

b = str()
for i in range(len(numList[1])) :
  b += numList[1][i]
int(b)

print( a if a > b else b)
    

