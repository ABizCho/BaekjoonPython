for i in range(int(input())) :
  ox = input()
  ox = list(ox)
  cnt = 1
  sum = 0

  for j in range(len(ox)) :
    if ox[j] == 'O' :
      sum += cnt
      cnt += 1
    
    else : 
      cnt = 1

  print(sum)

    


