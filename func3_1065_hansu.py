N = int(input())
total_cnt = 0

for i in range(1,N+1) : 

  c_list = list(str(i))

  dif_list = list()

  cnt = 0

  if len(c_list) == 1 or len(c_list) == 2 :
    total_cnt += 1

  else :
    #
    for i in range(len(c_list)):
      c_list[i] = int(c_list[i]) #char를 int로 변환저장

    firstDif = c_list[1] - c_list[0]
    
    for c in range(1, len(c_list)-1) : #차이의 수이므로 -1, 또한 이미 첫번째 차값을 반복 앞에서 구해놨으므로 -1, 총 charList 길이의 -2만큼 반복한다
      if firstDif == c_list[c+1] -c_list[c]  :
        cnt += 1
      else : 
        break
    if cnt == len(c_list) - 2 :
      total_cnt += 1


print(total_cnt)