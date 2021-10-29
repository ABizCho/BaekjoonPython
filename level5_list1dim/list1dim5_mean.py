#입력
import sys
input = sys.stdin.readline

intScoreN = int(input())

intListScore = list()
intListScore.extend(map(int,input().split()))

intScoreMax = max(intListScore)

#처리및출력

for i in range(len(intListScore)) :
  intListScore[i] = intListScore[i] / intScoreMax * 100

print(sum(intListScore)/intScoreN)