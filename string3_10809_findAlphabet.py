# a:97 ~ z:122
#1.
# (1)입력받은 문자열을 리스트로 변환
# (2)리스트 원소를 아스키코드로 변환
inputList = list( map( ord, list( input() ) ) )

for i in range(97,123) :
  for j in range(len(inputList)) :
    dif = -1
    if inputList[j] == i :
      dif = j
      break
  print(dif,end=' ')



####
# inputWord = input()

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for i in alphabet :
#   pV = -1
#   if inputWord.find(i) == True :
#     pV = inputWord.find(i)

#   print(pV,end = ' ')



