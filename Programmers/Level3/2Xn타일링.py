# 피보나치 수열을 사용한 풀이
# 1, 2, 3, 5, 7,....
def solution(n):
    a, b = 1, 1
    
    for i in range(n):
        a, b = b, a+b
    
    return a % 1000000007
