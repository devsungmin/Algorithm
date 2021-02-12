# 1,2,4만을 사용 가능 -> 3진수
def solution(n):
    ternary_number = ['1','2','4'];
    result = ''
    
    while n > 0:
        n -= 1
        result = ternary_number[n%3] + result
        n //= 3
        
    return result
