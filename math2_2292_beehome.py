N = 21

cnt = 1
hexa = 6
i = 1

while i < N :
  cnt += 1

  i += hexa
  hexa += 6

print(cnt)