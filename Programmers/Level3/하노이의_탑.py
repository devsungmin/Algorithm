# 재귀를 사용
# 전역변수를 사용하고 global을 사용하여 각 함수에서도 값을 바꿀 수 있도록 선언
result = []

def hanoi(n, start, end, mid):
    global result
    
    if n == 1:
        result.append([start, end])
    else:
        hanoi(n-1 , start, mid, end)
        result.append([start, end])
        hanoi(n-1, mid, end, start)
    
    return result

def solution(n):
    global result
    
    hanoi(n, 1, 3, 2)
    
    return result
