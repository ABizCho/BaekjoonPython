N = int(input())

for i in range(N) :
    
  inputV = list()
  inputV.extend( input().split(' ') )
  #print(inputV)

  inputV = [ [int(inputV[0])], list(inputV[1]) ]

  for i in range( len(inputV[1])) :
    for j in range(inputV[0][0]) :
      print(inputV[1][i],end='')
  print('')     

