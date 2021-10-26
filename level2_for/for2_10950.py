#테스트수 입력
inputT = int(input())


#테스트 케이스 입력 by 2차원 리스트
ABlist = [[0 for j in range(2)] for i in range(inputT)]
#print(ABlist)

for i in range(0,inputT) :
  ABlist[i][0],ABlist[i][1]= map(int,input().split())

#처리 및 출력

for i in range(0,inputT) :
  print(ABlist[i][0]+ABlist[i][1])