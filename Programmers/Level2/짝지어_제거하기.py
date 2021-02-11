# stack을 사용해서 비교하여 풀이 진행
def solution(s):
    stack = []
    
    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
            
    if len(stack) >= 1:
        return 0
    else:
        return 1
