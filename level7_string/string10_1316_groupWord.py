N = int(input())
total_cnt = 0

for i in range(N) :
  word = list(input())
  
  keep = list()
  lag = 0
  errors = 0

  for j in range(len(word)) :
    if word[j] in keep :
      if word[j] == lag :
        continue
      elif word[j] != lag :
        errors += 1
        break
    elif word[j] not in keep :
      
      keep.append(word[j])
      
      lag = word[j]
      continue
  if errors >= 1 :
    continue
  elif errors == 0 :
    
    total_cnt += 1

print(total_cnt)
