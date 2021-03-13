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

# 올바른 괄호
def checkStr(p):
    stack = []

    for i in p:
        if i== '(':
            stack.append('i')
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True
            
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
        u, v = divide(p)
        if checkStr(u):
            answer += u
        else:
            answer += '(' + solution(v) + ')' + reverse(u[1:-1])
            break

    return answer