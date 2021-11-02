#다이얼 넘버 구현 
List = [[] for i in range(10)]

for i in range(1,10) :
  List[i-1].append(i)

List[9].append(0)

#
List[1].extend( list( map(chr,list(range(65,68)))))
List[2].extend( list( map(chr,list(range(68,71)))))
List[3].extend( list( map(chr,list(range(71,74)))))
List[4].extend( list( map(chr,list(range(74,77)))))
List[5].extend( list( map(chr,list(range(77,80)))))
List[6].extend( list( map(chr,list(range(80,84)))))
List[7].extend( list( map(chr,list(range(84,87)))))
List[8].extend( list( map(chr,list(range(87,91)))))

#입력 및 다이얼 소속 넘버 dialList에 append
dialList = list()

inS = list(input())

for i in inS :
  for j in range(len(List)) :
    if i in List[j] :
      dialList.append(List[j][0])
      continue

#다이얼 넘버에 +1하면 각다이얼별 소요시간이됨
for i in range(len(dialList)) :
  dialList[i] += 1

#다이얼 시간총계
print(sum(dialList))
