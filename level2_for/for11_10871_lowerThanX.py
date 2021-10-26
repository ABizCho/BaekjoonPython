#사전입출력설정
import sys
input = sys.stdin.readline

#입력
N,X = map(int,input().split())

#N개의 정수 저장공간 1차원리스트 생성
A = []

#수열을 이루는 정수 N개 입력 및 저장
A.extend(map(int,input().split())) #extend 메소드를 통해 여러개 원소를 리스트에 한번에 추가할 수 있음

#처리 및 출력
for i in A :
  if i < X :
    print(i,end=' ')