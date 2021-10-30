#테스트리스트
testlist = [1, 2, 3]
print('Test List : ',testlist,'\n')

#임의 사용자함수
def plus1(a) :
  return a+1

# map으로 적용
print('list(map( 리스트원소 각각을 인자로 실행될 함수 , 리스트 )) 적용 : ',list( map( plus1 , testlist) ),'\n')

# map을 list()로 감싸지 않았을 경우
print('list()로 감싸지 않았을 경우 : ',map( plus1 , testlist),'\n')

