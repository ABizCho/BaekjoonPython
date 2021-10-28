#입출력사전설정
import sys
input = sys.stdin.readline

N = int(input()) #횟수 입력

list1dim = [] #1차원리스트생성
list1dim.extend(map(int,input().split())) #리스트에 extend 메소드 이용하여 저장공간에 맞게 순차적으로 분할저장

print(min(list1dim),max(list1dim)) #max,min method 사용