"""
참고 자료
https://johnyejin.tistory.com/124
"""

# 올바른 괄호
def check(p):
    stack = []
    try:
        for i in p:
            if i == '(':
                stack.append('i')
            else:
                stack.pop()
        return True
    except:
        return False

# 문자열 분리
def divide(p):
    idx = [0, 0]
    for i in p:
        if i == '(':
            idx[0] += 1
        else:
            idx[1] += 1
        if idx[0] == idx[1]:
            break
    return p[:sum(idx)], p[sum(idx):]



# 괄호 방향 바꾸기
def reverse(u):
    tmp = ''
    for i in u:
        if i == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp

def solution(p):
    answer = ''

    while len(p) != 0:
        u, p = divide(p)
        if check(u):
            answer += u
        else:
            answer += '(' + solution(p) + ')' + reverse(u[1:-1])
            break

    return answer