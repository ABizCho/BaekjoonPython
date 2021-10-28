'''
#러닝타임측정 사전작업
import time
import datetime


#러닝타임측정시작
start = time.time()
'''

'''
#방법1
list1dim = []
i = 0
intHigher = 0
indexH = 0

while 1 :
  try : 
    list1dim.append(int(input()))
  except :
    break
  
  if i == 0 :
    intHigher = list1dim[i]
  
  else :
    if list1dim[i] > intHigher : 
      intHigher = list1dim[i]
      indexH = i+1

  i += 1

print(intHigher)
print(indexH)
'''

#방법2
list1dim= []

while 1 :
  try :
    list1dim.append(int(input()))
  except :
    break

print(max(list1dim))

for i in range(len(list1dim)) :
  if list1dim[i] == max(list1dim) :
    print(i+1)
    break


'''
#러닝타임 후작업
sec = time.time()-start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)
'''

