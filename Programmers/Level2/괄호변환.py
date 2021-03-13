# 2번 문자열 분리
def divide(p):
    str_divide = [0,0]
    for i in p:
        if i == '(':
            str_divide[0] += 1
        else:
            str_divide[1] += 1
        if str_divide[0] == str_divide[1]:
            break
    return p[:sum(str_divide)], p[sum(str_divide):]

# 3번 올바른 괄호
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

# 4번 괄호 방향 바꾸기
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
    
    if len(p) == 0:
        return ""
    
    while p:
        # 문자열 분리
        u,v = divide(p)
        # 올바른 괄호 인지 확인
        if checkStr(u):
            answer += u
        else:
            answer += '(' + solution(p) + ')' + reverse(u[1:-1])
            break
        
    return answer