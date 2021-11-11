#
word = list(input().upper())
uniqueWord = list(set(word))

cnt = 0
final = 0

for u in uniqueWord :
  if cnt < word.count(u) :
    cnt = word.count(u)
    final = u

  elif cnt == word.count(u) :
    final = "?"
  
  else :
    continue

print(final)

#######
# for u in uniqueWord : 
#   if u in wordCnt == True :
#     continue
#   else:
#     wordCnt.append(u)
#     if cnt < word.count(u) :
#       cnt = word.count(u)
#       finalPrint = u
#     elif cnt == word.count(u) :
#       finalPrint = "?"

# print(finalPrint)
######
#   wordCnt.append(upperCaseAscii.find(w))

# Higher = 0
# finalPrint = 0
# for w in wordCnt :
#   if Higher < wordCnt.counts(w) :
#     Higher = wordCnt.counts(w)
#     finalPrint = w

#   elif Higher == wordCnt.counts(w) :
#     finalPrint = 0
    
# ##
# if finalPrint == 0 :
#   print("?")
# elif finalPrint > 0 :
#   print(chr(finalPrint))