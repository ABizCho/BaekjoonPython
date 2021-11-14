for T in range(int(input())):
  k = int(input())
  n = int(input())

  klist = list(range(0,k+1))
  nlist = list(range(1,n+1))

  fList = list()
  fList.extend(nlist)  

  tempKlist = nlist
  
  for K in range(0,k) :
    
    for N in range(len(nlist)) :
      tempKlist.append(sum(tempKlist[0:N+1]))
    del tempKlist[0:n]
    
  print(tempKlist[n-1])





  









    

  

  
  

  