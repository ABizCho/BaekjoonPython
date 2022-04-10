N = int(input())
my_string_list = []

for i in range(N):
    my_string_list.append(input())              #우선 주어진 N개의 test case들을 모두 하나의 리스트에 집어넣는다.

def is_valid_ps(test_string):                   #주어진 괄호 문자열이 올바른 괄호 문자열인지를 검사하는 함수
    test_list = list(test_string)               #test case
    l = len(test_list)                         
    while len(test_list) > 0:                   
        if len(test_list) == 1:
            return "NO"
        is_change = False
        for i in range(l - 1):
            if i >= len(test_list) - 1:
                break
            if test_list[i] == '(' and test_list[i + 1] == ')':             #'(', ')'가 연이어 나오면 둘 다 삭제
                del (test_list[i + 1])
                del (test_list[i])
                is_change = True
        if is_change == False:                                              
            return "NO"
    return "YES"

for i in range(N):
    print(is_valid_ps(my_string_list[i]))