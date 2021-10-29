


#입출력사전설정
import sys
input = sys.stdin.readline

#입력
intList = list()
i = 0

#입력 저장
while 1 :
  try :
    intList.append(int(input()))
    intList[i] = intList[i] % 42
  except :
    break
  
  i += 1 

#방법 1 고민하다가 털림



# # #중복제거 알고리즘

# intListCopy = intList
# removeIndex = list()

# removeIndex2 = list()

# for i in range(len(intListCopy)) :
#   for j in range(0,len(intListCopy)) :
#     if intListCopy[i] == intListCopy[j] :
#       removeIndex.append(j)
#   removeIndex2.append(removeIndex)
#   removeIndex = list()

# print(removeIndex2)

# for i in range(len(removeIndex2)) :
#   if len(removeIndex2[i][])

      
# # while 1 :
# #   try :
# #     temp = intList[i]
# #     intList.remove(intList[i])
  
# #   except :
# #     if exitTarget == intList[0] :
# #       break
# #   print(intList)
# #   i 

  
intSet= set(intList)
print(len(intSet)) 