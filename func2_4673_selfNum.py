####첫시도 : 지저분하고 더럽고 실패함###
# def d(n) :
#   nList = list(str(n))
#   for i in range(len(nList)):
#     nList[i] = int(nList[i])
#   sumV = sum(nList)
#   result = n + sumV
#   return result
# #생성자로 만들어진 값들
# def selfNum() :
#   reList = list()
#   for i in range(1,10001) :
#     reList.append(d(i))

#   return reList

# print(selfNum()) #검증용

# #생성자가 없는 값들
# naturalNum = list(range(1,10001))

# def selfNumT() :
#   for i in naturalNum:
#     for j in range(len(selfNum())) :
#       if i == selfNum()[j] :
#         naturalNum.remove(i)

# selfNumT()
# print(naturalNum)==================


#short-cut으로 최종코드====
naturalNum = set(range(1,10001))
compareNum = set()

for i in range(1,10001):
  sum = 0
  for j in str(i) :
    sum += int(j)
  sum += int(i)
  
  compareNum.add(sum)

selfNum = sorted(naturalNum - compareNum)

for i in selfNum :
  print(i) 