A,B= map(str, input().split())

L = abs(len(A) - len(B))

if len(A) > len(B) : 
  Alist = list(A)
  Blist = [0 for i in range(L)]
  Blist.extend(B)
else :
  Blist = list(B)
  Alist = [0 for i in range(L)]
  Alist.extend(A)

Alist = list(map(int,Alist))
Blist = list(map(int,Blist))

#
Higher = Alist if len(A)>len(B) else Blist
sumList = list()
for i in range(1,len(Alist)+1) :
  sumList.insert(0,Alist[len(Alist) - i] +Blist[len(Blist) - i])

for i in range(1,len(sumList)) :
  if sumList[len(sumList)-i] >= 10 :
    sumList[len(sumList)-i-1] += sumList[len(sumList)-i] // 10
    sumList[len(sumList)-i] = sumList[len(sumList)-i] % 10

print( int( ''.join( list( map( str, sumList)))))